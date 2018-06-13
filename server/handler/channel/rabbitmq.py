#! -*- coding: utf-8 -*-


import pika
import time
import uuid


from server import settings
from server.common.logger import Logger
from server.common.amqp.sender import AMQPSender
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

    def events_filter(self, events):
        events_data = []
        # may be you want filter out event that half an hour ago
        for event_data in events:
            fname, fcontent = event_data
            mtimedelta = time.time() - self.wcache_handler.mtime(fname)
            if mtimedelta < settings.CHANNEL_SENDER_EVENT_EXPIRED_TIME:
                events_data.append(event_data)
                continue
            logger.warning('Expired event file %s, deleted', fname)
            self.wcache_handler.remove(fname)

        return events_data

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

    def publish_message(self):
        if self._stopping:
            return
        # default batch 50, can be set larger
        events_data = self.wcache_handler.read()
        events_data_filtered = self.events_filter(events_data)
        for fname, fcontent in events_data_filtered:
            # may be usefull
            # fpath = os.path.join(self.wcache_handler.cache_path, fname)
            self._channel.basic_publish(self._exchange, self._routing_key, fcontent, properties={})
            self._message_number += 1
            self._cache_confirm.update({self._message_number: fname})
            self._deliveries.append(self._message_number)
            logger.info('Published message # %i', self._message_number)
        self.schedule_next_message()

    def on_delivery_confirmation(self, method_frame):
        confirmed = super(RabbitMQChannelSender, self).on_delivery_confirmation(method_frame)
        if confirmed is False:
            return
        fname = self._cache_confirm.pop(method_frame.method.delivery_tag, '')
        self.wcache_handler.remove(fname)


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

    def on_message(self, unused_channel, basic_deliver, properties, body):
        logger.info('Received message # %s from %s: %s',
                    basic_deliver.delivery_tag, properties.app_id, body)
        # put it to local cache
        self.rcache_handler.write(body)
        self.acknowledge_message(basic_deliver.delivery_tag)


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
