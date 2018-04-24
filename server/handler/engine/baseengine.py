#! -*- coding: utf-8 -*-


import traceback

from server.util.logger import Logger
from server.handler.backend._redis import RedisBackendHandler
from server.handler.channel.rabbitmq import RabbitMQChannelHandler


logger = Logger.get_logger(__name__)


class BaseMetaClass(type):
    subclass = {}

    def __new__(cls, name, bases, attrs):
        klass = type.__new__(cls, name, bases, attrs)

        if name == 'BaseEngineHandler':
            return klass
        if klass.enable is False:
            return klass

        BaseMetaClass.subclass.update({klass.name: klass})

        return klass


class BaseEngineHandler(object):
    __metaclass__ = BaseMetaClass

    name = None
    enable = True

    def __init__(self, decrypt_factory=None, backend_handler=None,  channel_handler=None):
        self._decrypt_factory = decrypt_factory
        self._backend_handler = backend_handler
        self._channel_handler = channel_handler

    @property
    def real_name(self):
        name = '{0}.{1}'.format(self.__module__, self.__class__.__name__)

        return name

    @property
    def decrypt_factory(self):
        return self._decrypt_factory

    @property
    def backend_handler(self):
        if isinstance(self._backend_handler, RedisBackendHandler):
            return self._backend_handler
        self._backend_handler = RedisBackendHandler()

        return self._backend_handler

    @property
    def channel_handler(self):
        if isinstance(self._channel_handler, RabbitMQChannelHandler):
            return self._channel_handler
        self._channel_handler = RabbitMQChannelHandler()

        return self._channel_handler

    def dispose_notexists(self, event):
        event_name = event.get_event_name()
        message = 'No engine handler handle event: {0}'.format(event_name)

        logger.warning(message)

    def dispose_exception(self, event, message):
        target_host_id = event.get_target_host_id()
        target_cluster_id = event.get_target_cluster_id()
        target_hostgroup_id = event.get_target_hostgroup_id()

        _message = 'Hanlde  outer event: {0} (host: {1}, hostgroup: {1}, cluster: {2}) with exception: {3}'.format(
            event, target_host_id, target_hostgroup_id, target_cluster_id, message
        )
        logger.error(_message)

    def before_dispose(self, event):
        event_name = event.get_event_name()
        target_host_id = event.get_target_host_id()
        target_cluster_id = event.get_target_cluster_id()
        target_hostgroup_id = event.get_target_hostgroup_id()

        message = 'Start handle outer event: {0} (host: {1}, hostgroup: {1}, cluster: {2})'.format(
            event_name, target_host_id, target_hostgroup_id, target_cluster_id
        )
        logger.info(message)

    def after_dispose(self, event):
        event_name = event.get_event_name()
        target_host_id = event.get_target_host_id()
        target_cluster_id = event.get_target_cluster_id()
        target_hostgroup_id = event.get_target_hostgroup_id()

        message = 'Finish handle outer event: {0} (host: {1}, hostgroup: {1}, cluster: {2})'.format(
            event_name, target_host_id, target_hostgroup_id, target_cluster_id
        )
        logger.info(message)

    def handle(self, event):
        raise NotImplementedError

    def decrypt_data(self, event):
        encryption = event.get_encryption()
        event_data = event.get_event_data()
        # Todo:
        #   1. create decrypt handler with decrypt_factory
        #   2. decrypt event data

        return event_data

    def dispose(self, event):
        self.before_dispose(event)
        try:
            self.handle(event)
        except Exception as e:
            self.dispose_exception(event, e)
        finally:
            self.after_dispose(event)


class EngineHandlerFactory(object):
    def create_handler(self, name):
        name = name if name in BaseMetaClass.subclass else 'default'
        klss = BaseMetaClass.subclass.get(name)

        return klss()
