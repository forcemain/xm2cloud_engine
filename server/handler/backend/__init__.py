#! -*- coding: utf-8 -*-


class BaseBackendHandler(object):
    @property
    def pool(self):
        raise NotImplementedError


