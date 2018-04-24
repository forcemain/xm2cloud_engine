#! -*- coding: utf-8 -*-


import time

from server import settings
from server.util.logger import Logger
from server.models.metric_data import MetricData
from server.models.event.event_type import EventType
from server.handler.engine.baseengine import BaseEngineHandler


logger = Logger.get_logger(__name__)


class MonitoringEngineHandler(BaseEngineHandler):
    enable = True
    name = EventType.MONITORING

    def get_metric(self, event):
        event_data = event.get_event_data()
        metric = MetricData.from_json(event_data)

        if metric.is_valid():
            return metric
        logger.warning('{0} got invalid monitor event: {1}'.format(self.real_name, event_data))

        return

    def get_merge_tag(self, **kwargs):
        merge_tags = []
        for k, v in kwargs.iteritems():
            merge_tags.append('{0}={1}'.format(k, v))
        merged_tag = '/{0}'.format(','.join(merge_tags)) if merge_tags else ''

        return merged_tag

    def get_metric_key(self, metric, event):
        agent_uuid = event.get_agent_uuid()

        _name = metric.get_name()
        _tags = self.get_merge_tag(**metric.get_tags())
        metric_key = '{0}.{1}{2}'.format(agent_uuid, _name,  _tags)

        return metric_key

    def get_event_key(self, event):
        event_uuid = event.get_event_uuid()

        return event_uuid

    def put_event(self, event):
        metric = self.get_metric(event)
        if metric is None:
            return

        event_key = self.get_event_key(event)
        metric_key = self.get_metric_key(metric, event)
        event_timestamp = event.get_event_timestamp()

        pipe = self.backend_handler.pool.pipeline()
        key_numer = self.backend_handler.pool.zcard(metric_key)
        if key_numer > settings.BACKEND_PER_MAX_POINTS:
            pipe.zrem(metric_key, event_key)
            pipe.delete(event_key)
        _value = metric.get_value()
        pipe.zadd(metric_key, event_timestamp, event_key)
        pipe.hmset(event_key, {'value': _value})
        pipe.execute()

    def handle(self, event):
        self.put_event(event)

