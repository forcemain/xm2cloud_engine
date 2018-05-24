#! -*- coding: utf-8 -*-


import sys


from server.core.engine import Engine
from server.core.channel import Channel
from server.common.logger import Logger
from server.database import get_agentdir
from server.core.heatbeat import Heartbeat
from server.signals.exit import GracefulExitSignal


reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.insert(0, get_agentdir())


logger = Logger.get_logger(__name__)


class Server(object):
    def __init__(self, channel=None, engine=None, heatbeat=None):
        self._engine = engine
        self._channel = channel
        self._heatbeat = heatbeat

        self._gsignal = GracefulExitSignal()

    @property
    def engine(self):
        if isinstance(self._engine, Engine):
            return self._engine
        self._engine = Engine(self._gsignal)

        return self.engine

    @property
    def channel(self):
        if isinstance(self._channel, Channel):
            return self._channel
        self._channel = Channel(self._gsignal)

        return self._channel

    @property
    def heatbeat(self):
        if isinstance(self._heatbeat, Heartbeat):
            return self._heatbeat
        self._heatbeat = Heartbeat(self._gsignal)

        return self._heatbeat

    def run(self):
        self.engine.start()
        self.channel.start()
        self.heatbeat.start()

    def start(self):
        self.run()
        self._gsignal.register_workers(*[
            self.engine,
            self.channel,
            self.heatbeat
        ])

    def listening(self):
        self.start()
        self._gsignal.listening()

if __name__ == '__main__':
    Server().listening()
