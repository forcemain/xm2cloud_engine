#! -*- coding: utf-8 -*-


from server.handler.backend._redis import RedisBackendHandler
from server.handler.backend._opentsdb import OpenTSDBBackendHandler


class BackendHandlerFactory(object):
    def create_handler(self, name):
        handlers = {
            'redis': RedisBackendHandler,
            'opentsdb': OpenTSDBBackendHandler,
        }

        return handlers.get(name)()
