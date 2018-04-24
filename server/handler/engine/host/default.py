#! -*- coding: utf-8 -*-


from server.util.logger import Logger
from server.handler.engine.baseengine import BaseEngineHandler


logger = Logger.get_logger(__name__)


class DefaultEngineHandler(BaseEngineHandler):
    enable = True
    name = 'default'

    def dispose(self, event):
        self.dispose_notexists(event)
