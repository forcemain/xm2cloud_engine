#! -*- coding: utf-8 -*-


from server.models.heartbeat import Heartbeat


class HeartbeatHandler(object):
    def __init__(self):
        pass

    def run_executer(self):
        result = Heartbeat()

        return result
