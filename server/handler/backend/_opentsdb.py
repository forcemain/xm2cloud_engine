#! -*- coding: utf-8 -*-

import urllib3


from server import settings
from server.handler.backend import BaseBackendHandler


class OpenTSDBBackendHandler(BaseBackendHandler):
    def __init__(self):
        self._num_pools = settings.BACKEND_OPENTSDB_POOL_NUM

    @property
    def pool(self):
        return urllib3.PoolManager(num_pools=self._num_pools)
