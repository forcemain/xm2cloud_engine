#! -*- coding: utf-8 -*-


from server import settings
from urllib3 import PoolManager
from urllib3.util.timeout import Timeout
from server.handler.backend import BaseBackendHandler


class OpenTSDBBackendHandler(BaseBackendHandler):
    def __init__(self):
        self._num_pools = settings.BACKEND_OPENTSDB_POOL_NUM
        self._conn_timeout = settings.BACKEND_OPENTSDB_CONN_TIMEOUT
        self._read_timeout = settings.BACKEND_OPENTSDB_READ_TIMEOUT

    @property
    def pool(self):
        timeout = Timeout(connect=self._conn_timeout, read=self._read_timeout)
        return PoolManager(num_pools=self._num_pools, timeout=timeout)
