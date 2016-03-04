#!/usr/bin/env python
# coding=utf8

from pfrock_static_plugin.handlers import ROUTER_STATIC_FILE, ROUTER_STATIC_DIR, ROUTER_PATH, ROUTER
from pfrock_static_plugin.handlers.dir import FrockStaticDirHandler
from pfrock_static_plugin.handlers.file import FrockStaticFileHandler

STATIC_HANDLER_MAP = {
    ROUTER_STATIC_DIR: FrockStaticDirHandler.get_handler,
    ROUTER_STATIC_FILE: FrockStaticFileHandler.get_handler,
}


class PfrockStaticPlugin(object):
    def get_handler(self, options, **kwargs):
        handler_list = []

        # url path
        url_path = kwargs.get(ROUTER_PATH)

        # nesting config
        if ROUTER in options:
            for one_route in options[ROUTER]:
                cur_options = dict(options)
                cur_options.update(one_route)
                handler = self.__parser_one(url_path, cur_options)
                if handler:
                    handler_list.append(handler)
        else:
            handler = self.__parser_one(url_path, options)
            if handler:
                handler_list.append(handler)

        return handler_list

    def __parser_one(self, url_path, options):

        for handler_type in STATIC_HANDLER_MAP:
            if handler_type in options:
                return STATIC_HANDLER_MAP[handler_type](url_path, options)

        return None
