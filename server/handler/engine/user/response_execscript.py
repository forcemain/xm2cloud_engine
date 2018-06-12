#! -*- coding: utf-8 -*-


from server import settings
from server.common.logger import Logger
from server.models.event.event_type import EventType
from server.handler.engine.baseengine import BaseEngineHandler


logger = Logger.get_logger(__name__)


class HeartbeatEngineHandler(BaseEngineHandler):
    enable = True
    name = EventType.RESPONSE_EXECUTESCRIPT

    def __init__(self):
        super(HeartbeatEngineHandler, self).__init__()
        self.backend_handler = self.backend_factory.create_handler('redis')

    def get_response_code(self, event):
        response_code = event.get_response_code()

        return response_code

    def get_event_key(self, event):
        sevent_uuid = event.get_event_id()
        host_uuid = event.get_source_host_id()
        event_key = "{0}::{1}::{2}".format(settings.LOGGING_TASK_KEY_PREFIX, sevent_uuid, host_uuid)

        return event_key

    def put_event(self, event):
        event_key = self.get_event_key(event)
        response_code = self.get_response_code(event)

        # xm2cloud_agent::logging::key::f352c284-19f3-44ef-927e-8ad2eabdae94::f352c284-19f3-44ef-927e-8ad2eabdae94
        # {
        #     state: 1314
        # }
        pipe = self.backend_handler.pool.pipeline()
        pipe.hmset(event_key, {'state': response_code})
        pipe.execute()

    def handle(self, event):
        self.put_event(event)
