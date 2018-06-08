#! -*- coding: utf-8 -*-


import time


from server import settings
from server.common.logger import Logger
from server.models.event.handle_log import HandleLog
from server.models.event.event_type import EventType
from server.handler.engine.baseengine import BaseEngineHandler


logger = Logger.get_logger(__name__)


class LoggingEngineHandler(BaseEngineHandler):
    enable = True
    name = EventType.LOGGING

    def __init__(self):
        super(LoggingEngineHandler, self).__init__()
        self.backend_handler = self.backend_factory.create_handler('redis')

    def get_logging(self, event):
        event_data = self.decrypt_data(event)
        logging = HandleLog.from_json(event_data)

        if logging.is_valid():
            return logging
        logger.warning('{0} got invalid logging event: {1}'.format(self.real_name, event_data))

        return

    def get_event_key(self, event):
        sevent_uuid = event.get_event_id()
        host_uuid = event.get_source_host_id()
        event_key = "xm2cloud_agent::logging::val::{0}::{1}".format(sevent_uuid, host_uuid)

        return event_key

    def put_event(self, event):
        event_key = self.get_event_key(event)
        logging_event = self.get_logging(event)
        event_timestamp = event.get_event_timestamp()

        if not logging_event:
            return

        logging_message = logging_event.get_message()
        # xm2cloud_agent::logging::val::f352c284-19f3-44ef-927e-8ad2eabdae94::f352c284-19f3-44ef-927e-8ad2eabdae94
        # [
        #   1528436631 'Start handle...'
        # ]

        pipe = self.backend_handler.pool.pipeline()
        pipe.zadd(event_key, event_timestamp, logging_message)
        pipe.execute()

    def handle(self, event):
        self.put_event(event)
