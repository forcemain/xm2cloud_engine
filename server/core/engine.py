#! -*- coding: utf-8 -*-


import os
import time


from server import settings
from threading import Thread
from server.util.enhance import File
from multiprocessing import Process
from server.util.logger import Logger
# autodiscovery engine handler
from server.handler.engine import host
from server.handler.engine import user
from datetime import datetime, timedelta
from server.models.event.pub_event import PubEvent
from server.exceptions import GracefulExitException
from server.handler.engine.baseengine import EngineHandlerFactory
from server.handler.channel.rabbitmq import RabbitMQChannelHandler


_evnet_threads = []


logger = Logger.get_logger(__name__)


class EventThread(Thread):
    def __init__(self, event_data, obj):
        super(EventThread, self).__init__()

        self._obj = obj
        self._fname, self._fcontent = event_data

    def after_run(self):
        if self in _evnet_threads:
            _evnet_threads.remove(self)
        self._obj.channel_handler.ccache_handler.remove(self._fname)

    def before_run(self):
        source_file = self._obj.channel_handler.rcache_handler.abspath(self._fname)
        target_file = self._obj.channel_handler.ccache_handler.abspath(self._fname)

        File.force_move(source_file, target_file)

    def run(self):
        self.before_run()
        try:
            event = PubEvent.from_json(self._fcontent)
            self._obj.event_dispatch(event)
        except Exception as e:
            logger.error('Handler %s got unexpected Exception %s', self._fname, e)
        finally:
            self.after_run()


class Engine(Process):
    def __init__(self, gsignal, engine_factory=None, channel_handler=None):
        super(Engine, self).__init__()

        self._gsignal = gsignal
        self._engine_factory = engine_factory
        self._channel_handler = channel_handler

    @property
    def engine_factory(self):
        if isinstance(self._engine_factory, EngineHandlerFactory):
            return self._engine_factory
        self._engine_factory = EngineHandlerFactory()

        return self._engine_factory

    @property
    def channel_handler(self):
        if isinstance(self._channel_handler, RabbitMQChannelHandler):
            return self._channel_handler
        self._channel_handler = RabbitMQChannelHandler()

        return self._channel_handler

    @property
    def next_scheduled(self):
        next_time = datetime.now() + timedelta(seconds=settings.ENGINE_SCHEDULER_INTERVAL)
        next_time_str = next_time.strftime('%Y-%m-%d %H:%M:%S')

        return next_time_str

    def run_destructor(self):
        self.channel_handler.ccache_handler.clear()

    def event_get(self):
        # default batch is 50, can be set larger
        events_data = self.channel_handler.rcache_handler.read(batch=128)

        return events_data

    def allow_dispatch(self, event):
        is_allow = True

        if not event.is_valid():
            is_allow = False
            logger.warning('Invalid engine event data: {0}'.format(event))

        return is_allow

    def event_dispatch(self, event):
        if not self.allow_dispatch(event):
            return
        try:
            event_name = event.get_event_name()
            handler = self.engine_factory.create_handler(event_name)
            handler.dispose(event)
        except Exception as e:
            logger.error('Handle event: {0} with exception: {1}'.format(event, e))
        finally:
            pass

    def run(self):
        try:
            while not self._gsignal.is_set():
                need_wait = False
                events_data = self.event_get()
                if len(events_data) == 0:
                    need_wait = True
                    logger.info('No events ready, next scheduled at %s', self.next_scheduled)
                if len(_evnet_threads) > settings.ENGINE_MAX_THREADPOOL_SIZE:
                    need_wait = True
                    logger.info('To many threads, next scheduled at %s', self.next_scheduled)
                if need_wait is True:
                    time.sleep(settings.ENGINE_SCHEDULER_INTERVAL)
                    continue
                for event_data in events_data:
                    t = EventThread(event_data, self)
                    t.setDaemon(True)
                    t.start()
                    _evnet_threads.append(t)
                    # may be an  time-consuming task, so not join
                logger.info('Events ready, next scheduled at %s', self.next_scheduled)
                time.sleep(settings.ENGINE_SCHEDULER_INTERVAL)
            print 'Engine process({0}) exit.'.format(os.getpid())
        except GracefulExitException:
            print 'Engine process({0}) got GracefulExitException.'.format(os.getpid())
        except Exception as e:
            print 'Engine process({0}) got unexpected Exception {1}'.format(os.getpid(), e)
        finally:
            self.run_destructor()

