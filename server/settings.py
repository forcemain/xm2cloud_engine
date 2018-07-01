#! -*- coding: utf-8 -*-


import logging


from multiprocessing import cpu_count


# Debug Settings
DEBUG = True

# Event Settings
EVENT_EXPIRED_TIME = 1800


# Engine Settings
ENGINE_SCHEDULER_INTERVAL = 1
ENGINE_MAX_THREADPOOL_SIZE = cpu_count()*32
ENGINE_EVENT_BATCH_SIZE = ENGINE_MAX_THREADPOOL_SIZE


# Heartbeat Settings
HEARTBEAT_EXPIRED_TIME = 180
HEARTBEAT_SCHEDULER_INTERVAL = 3


# Backend Settings
# Backend Redis Settnigs
BACKEND_REDIS_DB = 0
BACKEND_REDIS_PORT = 6379
BACKEND_MEMBER_PERIOD = 1*60*60
BACKEND_REDIS_MAX_CONNECTIONS = 10
BACKEND_REDIS_HOST = 'ops.xxoo.com'
BACKEND_REDIS_PASSWORD = 'z6A1kaff8X4UbsjpwxseMVtWerMxiAok'
# Backend OpenTsdb Settings
BACKEND_OPENTSDB_PORT = 4242
BACKEND_OPENTSDB_USERNAME = ''
BACKEND_OPENTSDB_PASSWORD = ''
BACKEND_OPENTSDB_PROTOCOL = 'http'
BACKEND_OPENTSDB_CONN_TIMEOUT = 2.0
BACKEND_OPENTSDB_READ_TIMEOUT = 5.0
BACKEND_OPENTSDB_HOST = 'ops.xxoo.com'
BACKEND_OPENTSDB_POOL_NUM = cpu_count()*10


# Channel Settings
CHANNEL_SCHEDULER_INTERVAL = 3
CHANNEL_SENDER_DISCONNECT_TIME = 120
CHANNEL_SENDER_EVENT_BATCH_SIZE = 200
CHANNEL_RECEIVER_DISCONNECT_TIME = 120
# Channel Kafka Settings
# Channel Rabbitmq Settings
CHANNEL_RABBITMQ_SSL = False
CHANNEL_RABBITMQ_PORT = 5672
CHANNEL_RABBITMQ_HOST = 'ops.xxoo.com'
CHANNEL_RABBITMQ_VHOST = '/event_engine'
CHANNEL_RABBITMQ_UP_EXCHANGE_TYPE = 'direct'
CHANNEL_RABBITMQ_UP_QUEUE = 'event_up_queue'
CHANNEL_RABBITMQ_AUTH_USER = 'event_engine_user'
CHANNEL_RABBITMQ_UP_EXCHANGE = 'event_up_exchange'
CHANNEL_RABBITMQ_UP_ROUTING_KEY = 'up_routing_key'
CHANNEL_RABBITMQ_DOWN_EXCHANGE = 'event_down_exchange'
CHANNEL_RABBITMQ_DOWN_ROUTING_KEY = 'down_routing_key'
CHANNEL_RABBITMQ_AUTH_PASS = 'oZ38h0GoA0TehWcAPyIJqaponqo8Itv9'


# Server Settings
SERVER_UUID = 'fdb747d1-505d-475c-828c-7bcb919162c6'


# Task settings
LOGGING_TASK_KEY_PREFIX = 'xm2cloud_agent::logging::key'
LOGGING_TASK_VAL_PREFIX = 'xm2cloud_agent::logging::val'
MONITORING_TASK_KEY_PREFIX = 'xm2cloud_agent::monitoring::key'
MONITORING_TASK_VAL_PREFIX = 'xm2cloud_agent::monitoring::val'


# Logging Settings
DEFAULT_LOG_LEVEL = logging.WARN
DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(pathname)s - %(lineno)d - %(levelname)s - %(message)s'
