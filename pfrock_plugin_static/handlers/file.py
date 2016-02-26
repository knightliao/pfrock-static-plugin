#!/usr/bin/env python
# coding=utf8
import os

from tornado import gen
from tornado.web import StaticFileHandler

from pfrock.core.constants import ROUTER_PATH
from pfrock_plugin_static.handlers import ROUTER_STATIC_FILE


class FrockStaticFileHandler(StaticFileHandler):
    def post(self):
        return self.get()

    def delete(self):
        return self.get()

    def put(self):
        return self.get()

    def initialize(self, path, default_filename=None, **kwargs):
        self.dir_name, self.file_name = os.path.split(path)
        super(FrockStaticFileHandler, self).initialize(self.dir_name)

    @gen.coroutine
    def get(self, path=None, include_body=True):
        # Ignore 'path'.
        super(FrockStaticFileHandler, self).get(self.file_name, include_body)

    @staticmethod
    def get_handler(url, options):
        file_path = options[ROUTER_STATIC_FILE] if ROUTER_STATIC_FILE in options else ""
        path = options[ROUTER_PATH] if ROUTER_PATH in options else ""

        if file_path and path:
            real_url = url[0:url.rfind('/') + 1] + path
            handler = (real_url, FrockStaticFileHandler, {ROUTER_PATH: file_path})
            return handler

        if file_path:
            handler = (url, FrockStaticFileHandler, {ROUTER_PATH: file_path})
            return handler

        return None
