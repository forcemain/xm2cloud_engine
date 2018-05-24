#! -*- coding: utf-8 -*-


import time


from server import settings
from server.common.logger import Logger
from server.models.heartbeat import Heartbeat
from server.models.event.event_type import EventType
from server.handler.engine.baseengine import BaseEngineHandler


logger = Logger.get_logger(__name__)


class HeartbeatEngineHandler(BaseEngineHandler):
    enable = True
    name = EventType.HEARTBEAT

    def __init__(self):
        super(HeartbeatEngineHandler, self).__init__()
        self.backend_handler = self.backend_factory.create_handler('redis')

    def get_heartbeat(self, event):
        event_data = self.decrypt_data(event)
        heartbeat = Heartbeat.from_json(event_data)

        if heartbeat.is_valid():
            return heartbeat
        logger.warning('{0} got invalid heartbeat event: {1}'.format(self.real_name, event_data))

        return

    def put_event(self, event):
        host_uuid = event.get_source_host_id()
        heartbeat = self.get_heartbeat(event)
        if heartbeat is None:
            return

        _timestamp = time.time()
        _name = heartbeat.get_name()
        _version = heartbeat.get_version()

        # xm2cloud_agent::heartbeat::f352c284-19f3-44ef-927e-8ad2eabdae94
        # xm2cloud_engine::heartbeat::f352c284-19f3-44ef-927e-8ad2eabdae94
        #
        ekey = '{0}::{1}::{2}'.format(_name, EventType.HEARTBEAT, host_uuid)
        pipe = self.backend_handler.pool.pipeline()
        pipe.hmset(ekey, {
            'timestamp': _timestamp,
            'name': _name, 'version': _version
        })
        pipe.expire(ekey, settings.HEARTBEAT_EXPIRED_TIME)
        pipe.execute()

    def handle(self, event):
        self.put_event(event)





