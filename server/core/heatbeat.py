#! -*- coding: utf-8 -*-


import os
import time


from server import settings
from multiprocessing import Process
from server.util.logger import Logger
from datetime import datetime, timedelta
from server.exceptions import GracefulExitException
from server.handler.heartbeat import HeartbeatHandler
from server.handler.event.heatbeat import HeatbeatEventHandler
from server.handler.channel.rabbitmq import RabbitMQChannelHandler


logger = Logger.get_logger(__name__)


class Heartbeat(Process):
    def __init__(self, gsignal, heartbeat_handler=None, event_handler=None, channel_handler=None):
        super(Heartbeat, self).__init__()
        self._gsignal = gsignal
        self._event_handler = event_handler
        self._channel_handler = channel_handler
        self._heartbeat_handler = heartbeat_handler

    @property
    def heartbeat_handler(self):
        if isinstance(self._heartbeat_handler, HeartbeatHandler):
            return self._heartbeat_handler
        self._heartbeat_handler = HeartbeatHandler()

        return self._heartbeat_handler

    @property
    def event_handler(self):
        if isinstance(self._event_handler, HeatbeatEventHandler):
            return self._event_handler
        self._event_handler = HeatbeatEventHandler()

        return self._event_handler

    @property
    def channel_handler(self):
        if isinstance(self._channel_handler, RabbitMQChannelHandler):
            return self._channel_handler
        self._channel_handler = RabbitMQChannelHandler()

        return self._channel_handler

    @property
    def next_scheduled(self):
        next_time = datetime.now() + timedelta(seconds=settings.HEARTBEAT_SCHEDULER_INTERVAL)
        next_time_str = next_time.strftime('%Y-%m-%d %H:%M:%S')

        return next_time_str

    def run_destructor(self):
        pass

    def event_put(self, ins):
        if not ins.is_valid():
            logger.warning('Invalid heartbeat event data: {0}'.format(ins))
            return
        logger.debug('Verified monitor event data: {0}'.format(ins))
        event = self.event_handler.create_event(ins.to_json())

        self.channel_handler.rcache_handler.write(event.to_json())

    def run(self):
        try:
            while not self._gsignal.is_set():
                self.event_put(self.heartbeat_handler.run_executer())
                logger.info('Events ready, next scheduled at %s', self.next_scheduled)
                time.sleep(settings.HEARTBEAT_SCHEDULER_INTERVAL)
            print 'Heartbeat process({0}) exit.'.format(os.getpid())
        except GracefulExitException:
            print 'Heartbeat process({0}) got GracefulExitException.'.format(os.getpid())
        except Exception as e:
            print 'Heartbeat process({0}) got unexpected Exception {1}'.format(os.getpid(), e)
        finally:
            self.run_destructor()

