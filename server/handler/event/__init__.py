#! -*- coding: utf-8 -*-


class BaseEventHandler(object):
    def encrypt_data(self, data):
        enc_method = None

        return enc_method, data

    def create_event(self, *args, **kwargs):
        raise NotImplementedError
