#! -*- coding: utf-8 -*-


import json

from server.models import BaseModel


class MetricData(BaseModel):
    def __init__(self, name=None, tags={}, value=None):
        self.name = name
        self.tags = tags
        self.value = value

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_tags(self):
        return self.tags

    def set_tags(self, tags):
        self.tags = tags

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def is_valid(self):
        return True

    def to_dict(self):
        data = {
            'name': self.get_name(),
            'tags': self.get_tags(),
            'value': self.get_value()
        }

        return data

    def to_json(self, indent=4):
        dict_data = self.to_dict()
        json_data = json.dumps(dict_data, indent=indent)

        return json_data

    @staticmethod
    def from_dict(data):
        event = MetricData()
        map(lambda r: setattr(event, r[0], r[1]), data.iteritems())

        return event

    @staticmethod
    def from_json(data):
        dict_data = json.loads(data)
        event = MetricData.from_dict(dict_data)

        return event
