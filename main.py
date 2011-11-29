#!/usr/bin/env python
# encoding: utf-8

"""
main.py
Created by dn on 2011-07-24.
Copyright (c) 2011 shubz. All rights reserved.
"""
import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import options

from config.urls import routes
from config.settings import settings_dict

class Application(tornado.web.Application):
    def __init__ (self):
        settings = settings_dict
        handlers = routes
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
