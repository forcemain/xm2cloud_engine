#! -*- coding: utf-8 -*-


import pika
import time


from server import settings
from server.common.logger import Logger
from server.common.amqp.sender import AMQPSender
from server.models.event.pub_event import PubEvent
from server.common.amqp.receiver import AMQPReceiver
from server.handler.channel import BaseChannelHelper, BaseChannelHandler


logger = Logger.get_logger(__name__)


class RabbitMQChannelSender(BaseChannelHelper, AMQPSender):
    def __init__(self, **kwargs):
        AMQPSender.__init__(self, **kwargs)
        BaseChannelHelper.__init__(self, **kwargs)

        self._cache_confirm = {}
        self._ssl = settings.CHANNEL_RABBITMQ_SSL
        self._host = settings.CHANNEL_RABBITMQ_HOST
        self._port = settings.CHANNEL_RABBITMQ_PORT
        self._vhost = settings.CHANNEL_RABBITMQ_VHOST
        self._queue = settings.CHANNEL_RABBITMQ_DOWN_QUEUE
        self._auth_user = settings.CHANNEL_RABBITMQ_AUTH_USER
        self._auth_pass = settings.CHANNEL_RABBITMQ_AUTH_PASS
        self._exchange = settings.CHANNEL_RABBITMQ_DOWN_EXCHANGE
        self._routing_key = settings.CHANNEL_RABBITMQ_DOWN_ROUTING_KEY
        self._exchange_type = settings.CHANNEL_RABBITMQ_DOWN_EXCHANGE_TYPE

    def connect(self):
        conn_parameters = pika.ConnectionParameters(
            ssl=self._ssl,
            host=self._host,
            port=self._port,
            retry_delay=5,
            channel_max=1000,
            socket_timeout=15,
            heartbeat_interval=10,
            connection_attempts=5,
            virtual_host=self._vhost,
            credentials=pika.PlainCredentials(self._auth_user, self._auth_pass),
        )

        logger.info('Connecting to {0}:{1}'.format(self._host, self._port))
        return pika.SelectConnection(conn_parameters,
                                     self.on_connection_open,
                                     stop_ioloop_on_close=True)

    def allow_send(self, fcontent):
        try:
            event = PubEvent.from_json(fcontent)
        except Exception as e:
            logger.warning('Invalid event: {0} with exception: {1}'.format(fcontent, e))
            return False

        return event.is_valid() and not event.is_expired()

    def publish_message(self):
        if self._stopping:
            return
        # default batch 50, can be set larger
        events_data = self.wcache_handler.read(batch=settings.CHANNEL_SENDER_EVENT_BATCH_SIZE)
        for fname, fcontent in events_data:
            if not self.allow_send(fcontent):
                logger.warning('Not allowed send this event data: {0}'.format(fcontent))
                continue
            # fpath = os.path.join(self.wcache_handler.cache_path, fname)
            self._channel.basic_publish(self._exchange, self._routing_key, fcontent, properties={})
            self.wcache_handler.remove(fname)
        self.schedule_next_message()


class RabbitMQChannelReceiver(BaseChannelHelper, AMQPReceiver):
    def __init__(self, **kwargs):
        AMQPReceiver.__init__(self, **kwargs)
        BaseChannelHelper.__init__(self, **kwargs)

        self._ssl = settings.CHANNEL_RABBITMQ_SSL
        self._host = settings.CHANNEL_RABBITMQ_HOST
        self._port = settings.CHANNEL_RABBITMQ_PORT
        self._vhost = settings.CHANNEL_RABBITMQ_VHOST
        self._queue = settings.CHANNEL_RABBITMQ_UP_QUEUE
        self._auth_user = settings.CHANNEL_RABBITMQ_AUTH_USER
        self._auth_pass = settings.CHANNEL_RABBITMQ_AUTH_PASS
        self._exchange = settings.CHANNEL_RABBITMQ_UP_EXCHANGE
        self._routing_key = settings.CHANNEL_RABBITMQ_UP_ROUTING_KEY
        self._exchange_type = settings.CHANNEL_RABBITMQ_UP_EXCHANGE_TYPE

    def connect(self):
        conn_parameters = pika.ConnectionParameters(
            ssl=self._ssl,
            host=self._host,
            port=self._port,
            retry_delay=5,
            channel_max=1000,
            socket_timeout=15,
            heartbeat_interval=10,
            connection_attempts=5,
            virtual_host=self._vhost,
            credentials=pika.PlainCredentials(self._auth_user, self._auth_pass),
        )

        logger.info('Connecting to {0}:{1}'.format(self._host, self._port))
        return pika.SelectConnection(conn_parameters,
                                     self.on_connection_open,
                                     stop_ioloop_on_close=True)

    def allow_receive(self, fcontent):
        try:
            event = PubEvent.from_json(fcontent)
        except Exception as e:
            logger.warning('Invalid event: {0} with exception: {1}'.format(fcontent, e))
            return False

        return event.is_valid()

    def on_message(self, unused_channel, basic_deliver, properties, body):
        logger.info('Received message # %s from %s: %s',
                    basic_deliver.delivery_tag, properties.app_id, body)
        if not self.allow_receive(body):
            logger.warning('Not allowed receive this event data: {0}'.format(body))
            return
        # put it to local cache
        self.rcache_handler.write(body)


class RabbitMQChannelHandler(BaseChannelHelper, BaseChannelHandler):
    def __init__(self, **kwargs):
        BaseChannelHelper.__init__(self, **kwargs)
        BaseChannelHandler.__init__(self, **kwargs)

    @property
    def msg_receiver(self):
        if isinstance(self._msg_receiver, AMQPReceiver):
            return self._msg_receiver
        self._msg_receiver = RabbitMQChannelReceiver()

        return self._msg_receiver

    @property
    def msg_sender(self):
        if isinstance(self._msg_sender, AMQPSender):
            return self._msg_sender
        self._msg_sender = RabbitMQChannelSender()

        return self._msg_sender
