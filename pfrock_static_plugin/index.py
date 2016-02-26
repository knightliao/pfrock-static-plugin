#!/usr/bin/env python
# coding=utf8
from pfrock.core.constants import ROUTER, ROUTER_PATH
from pfrock.core.plugin import PfrockPlugin
from pfrock_static_plugin.handlers import ROUTER_STATIC_FILE, ROUTER_STATIC_DIR
from pfrock_static_plugin.handlers.dir import FrockStaticDirHandler
from pfrock_static_plugin.handlers.file import FrockStaticFileHandler

STATIC_HANDLER_MAP = {
    ROUTER_STATIC_DIR: FrockStaticDirHandler.get_handler,
    ROUTER_STATIC_FILE: FrockStaticFileHandler.get_handler,
}


class PfrockStaticPlugin(PfrockPlugin):
    def get_handler(self, options, **kwargs):
        handler_list = []

        # url path
        url_path = kwargs.get(ROUTER_PATH)

        # nesting config
        if ROUTER in options:
            for route in options[ROUTER]:
                handler = self.__parser_one(url_path, route)
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
