#! -*- coding: utf-8 -*-


from redis import StrictRedis
from server import settings
from server.handler.backend import BaseBackendHandler


class RedisBackendHandler(BaseBackendHandler):
    def __init__(self):
        self._pool = None
        self._db = settings.BACKEND_REDIS_DB
        self._host = settings.BACKEND_REDIS_HOST
        self._port = settings.BACKEND_REDIS_PORT
        self._password = settings.BACKEND_REDIS_PASSWORD
        self._max_connections = settings.BACKEND_REDIS_MAX_CONNECTIONS

    @property
    def pool(self):
        if isinstance(self._pool, StrictRedis):
            return self._pool
        self._pool = StrictRedis(db=self._db,
                                 host=self._host,
                                 port=self._port,
                                 password=self._password,
                                 max_connections=self._max_connections)

        return self._pool
