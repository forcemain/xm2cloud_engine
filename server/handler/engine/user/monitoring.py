#! -*- coding: utf-8 -*-


import time
import json
import base64


from server import settings
from threading import Thread
from server.common.logger import Logger
from server.models.metric_data import MetricData
from server.models.event.event_type import EventType
from server.handler.engine.baseengine import BaseEngineHandler


logger = Logger.get_logger(__name__)


class BaseDataEngineHandler(object):
    @property
    def real_name(self):
        name = '{0}.{1}'.format(self.__module__, self.__class__.__name__)

        return name

    def get_metric(self, event):
        event_data = event.get_event_data()
        metric = MetricData.from_json(event_data)

        if metric.is_valid():
            return metric
        logger.warning('{0} got invalid monitor event: {1}'.format(self.real_name, event_data))

        return


class RedisDataEngineHandler(BaseDataEngineHandler):
    enable = True
    
    def __init__(self, backend_handler):
        super(RedisDataEngineHandler, self).__init__()
        self.backend_handler = backend_handler

    def get_merge_tag(self, **kwargs):
        merge_tags = []
        for k, v in kwargs.iteritems():
            merge_tags.append('{0}={1}'.format(k, v))
        merged_tag = '/{0}'.format(','.join(merge_tags)) if merge_tags else ''

        return merged_tag

    def get_metric_key(self, metric, event):
        host_uuid = event.get_source_host_id()

        _name = metric.get_name()
        _tags = self.get_merge_tag(**metric.get_tags())
        metric_key = '{0}::{1}.{2}{3}'.format(settings.MONITORING_TASK_KEY_PREFIX, host_uuid, _name,  _tags)

        return metric_key

    def get_event_key(self, event):
        event_uuid = event.get_event_uuid()
        event_key = "{0}::{1}".format(settings.MONITORING_TASK_VAL_PREFIX, event_uuid)

        return event_key

    def put_event(self, event):
        metric = self.get_metric(event)
        if not metric:
            return

        # # Timeseries(zadd):
        # xm2cloud_agent::monitoring::key::f352c284-19f3-44ef-927e-8ad2eabdae94.net.if.out.bytes.persec/iface=en2
        # [
        #     1524625902.152811 xm2cloud_agent::monitoring::val::55b71404-d994-401a-b4cc-857ce9b0e43b
        # ]
        # # Eventdata(hmset):
        # xm2cloud_agent::monitoring::val::55b71404-d994-401a-b4cc-857ce9b0e43b
        # {
        #     value: ...
        # }

        event_key = self.get_event_key(event)
        metric_key = self.get_metric_key(metric, event)
        event_timestamp = event.get_event_timestamp()

        pipe = self.backend_handler.pool.pipeline()
        _max = time.time() - settings.BACKEND_MEMBER_PERIOD
        pipe.zremrangebyscore(metric_key, 0, _max)

        _cache = 60
        _value = metric.get_value()
        pipe.zadd(metric_key, event_timestamp, event_key)
        pipe.hmset(event_key, {'value': _value})
        pipe.expire(event_key, settings.BACKEND_MEMBER_PERIOD+_cache)
        pipe.execute()

    def handle(self, event):
        self.put_event(event)


class OpenTSDBDataEngineHandler(BaseDataEngineHandler):
    enable = True

    def __init__(self, backend_handler):
        super(OpenTSDBDataEngineHandler, self).__init__()
        self.backend_handler = backend_handler

    def get_put_url(self):
        return '{0}://{1}:{2}/api/put?summary'.format(settings.BACKEND_OPENTSDB_PROTOCOL,
                                                      settings.BACKEND_OPENTSDB_HOST,
                                                      settings.BACKEND_OPENTSDB_PORT)

    def get_headers(self):
        headers = {'Content-Type': 'application/json'}
        if not settings.BACKEND_OPENTSDB_USERNAME or not settings.BACKEND_OPENTSDB_PASSWORD:
            return headers
        _encode_auth = base64.b64encode('{0}:{1}'.format(settings.BACKEND_OPENTSDB_USERNAME,
                                                         settings.BACKEND_OPENTSDB_PASSWORD))
        _authorization = 'Basic {0}'.format(_encode_auth)
        headers.update({'Authorization': _authorization})

        return headers

    def get_metric_data(self, metric, event):
        _tags = metric.get_tags()
        _metric = metric.get_name()
        _value = metric.get_value()
        _uuid = event.get_source_host_id()
        _timestamp = event.get_event_timestamp()

        _tags.update({'uuid': _uuid})
        #
        # {
        #     "metric": "net.if.in.bytes.persec",
        #     "timestamp": 1527153584,
        #     "value": 10000,
        #     "tags": {
        #         "uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94",
        #         "iface": "en0"
        #     }
        # }
        #
        return {'tags': _tags, 'value': _value, 'metric': _metric, 'timestamp': _timestamp}

    def put_event(self, event):
        metric = self.get_metric(event)
        if not metric:
            return
        put_url, headers, put_data = self.get_put_url(), self.get_headers(), self.get_metric_data(metric, event)
        self.backend_handler.pool.request('POST', put_url, body=json.dumps(put_data), headers=headers)

    def handle(self, event):
        self.put_event(event)


class MonitoringWriteThread(Thread):
    def __init__(self, event, handler, obj):
        super(MonitoringWriteThread, self).__init__()
        self._obj = obj
        self._event = event
        self._handler = handler

    def after_run(self):
        pass

    def before_run(self):
        pass

    def run(self):
        if not self._handler.enable:
            return
        self.before_run()
        try:
            self._handler.handle(self._event)
        except Exception as e:
            logger.error('Handler %s got unexpected Exception %s', self._event, e)
        finally:
            self.after_run()


class MonitoringEngineHandler(BaseEngineHandler):
    enable = True
    name = EventType.MONITORING

    def __init__(self):
        super(MonitoringEngineHandler, self).__init__()
        self.redis_backend_handler = self.backend_factory.create_handler('redis')
        self.opentsdb_backend_handler = self.backend_factory.create_handler('opentsdb')

    def handle(self, event):
        MonitoringWriteThread(event, RedisDataEngineHandler(self.redis_backend_handler), self).start()
        MonitoringWriteThread(event, OpenTSDBDataEngineHandler(self.opentsdb_backend_handler), self).start()


