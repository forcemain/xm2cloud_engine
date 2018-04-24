#! -*- coding: utf-8 -*-


import logging


from multiprocessing import cpu_count


# Debug Settings
DEBUG = True


# Engine Settings
ENGINE_SCHEDULER_INTERVAL = 1
ENGINE_MAX_THREADPOOL_SIZE = cpu_count()*32


# Heartbeat Settings
HEARTBEAT_EXPIRED_TIME = 180
HEARTBEAT_SCHEDULER_INTERVAL = 3


# Backend Settings
BACKEND_REDIS_DB = 0
BACKEND_REDIS_PORT = 6379
BACKEND_PER_MAX_POINTS = 250
BACKEND_REDIS_MAX_CONNECTIONS = 10
BACKEND_REDIS_HOST = 'ops.xm020.com'
BACKEND_REDIS_PASSWORD = 'z6A1kaff8X4UbsjpwxseMVtWerMxiAok'

# Channel Settings
CHANNEL_SCHEDULER_INTERVAL = 3
CHANNEL_SENDER_DISCONNECT_TIME = 120
CHANNEL_RECEIVER_DISCONNECT_TIME = 120
CHANNEL_SENDER_EVENT_EXPIRED_TIME = 1800
CHANNEL_RECEIVER_EVENT_EXPIRED_TIME = 1800
# Channel Kafka Settings
# Channel Rabbitmq Settings
CHANNEL_RABBITMQ_SSL = False
CHANNEL_RABBITMQ_PORT = 5672
CHANNEL_RABBITMQ_HOST = 'ops.xm020.com'
CHANNEL_RABBITMQ_VHOST = '/event_engine'
CHANNEL_RABBITMQ_EXCHANGE_TYPE = 'topic'
CHANNEL_RABBITMQ_UP_QUEUE = 'event_up_queue'
CHANNEL_RABBITMQ_DOWN_QUEUE = 'event_down_queue'
CHANNEL_RABBITMQ_AUTH_USER = 'event_engine_user'
CHANNEL_RABBITMQ_ROUTING_KEY = 'event_engine.rpc'
CHANNEL_RABBITMQ_UP_EXCHANGE = 'event_up_exchange'
CHANNEL_RABBITMQ_DOWN_EXCHANGE = 'event_down_exchange'
CHANNEL_RABBITMQ_AUTH_PASS = 'oZ38h0GoA0TehWcAPyIJqaponqo8Itv9'


# Server Settings
SERVER_UUID = 'fdb747d1-505d-475c-828c-7bcb919162c6'


# Logging Settings
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(pathname)s - %(lineno)d - %(levelname)s - %(message)s'
