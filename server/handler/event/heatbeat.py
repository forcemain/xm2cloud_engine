#! -*- coding: utf-8 -*-

import time


from server import settings
from server.common.enhance import Random
from server.handler.event import BaseEventHandler
from server.models.event.event_type import EventType
from server.models.event.pub_event import PubEvent


class HeatbeatEventHandler(BaseEventHandler):
    def create_event(self, data):
        event = PubEvent()

        event.set_event_uuid(Random.get_uuid())
        event.set_event_name(EventType.HEARTBEAT)
        event.set_event_timestamp(int(time.time()))
        event.set_source_host_id(settings.SERVER_UUID)

        # may be you want encrypt the data
        encryption, event_data = self.encrypt_data(data)
        event.set_encryption(encryption)
        event.set_event_data(event_data)

        return event

