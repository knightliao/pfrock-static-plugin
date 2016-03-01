#!/usr/bin/env python
# coding=utf8
import os

import tornado.gen
from tornado.web import StaticFileHandler

from pfrock_static_plugin.handlers import ROUTER_STATIC_FILE, ROUTER_PATH


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

    @tornado.gen.coroutine
    def get(self, path=None, include_body=True):
        # Ignore 'path'.
        try:
            yield super(FrockStaticFileHandler, self).get(self.file_name, include_body)
        except Exception, e:
            # when no found , return 404 just ok
            self.set_status(404)

    def compute_etag(self):
        """Sets the ``Etag`` header based on static url version.

        This allows efficient ``If-None-Match`` checks against cached
        versions, and sends the correct ``Etag`` for a partial response
        (i.e. the same ``Etag`` as the full file).

        .. versionadded:: 3.1
        """
        if not hasattr(self, 'absolute_path'):
            return None
        return super(FrockStaticFileHandler, self).compute_etag()

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
