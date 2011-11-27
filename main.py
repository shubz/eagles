#!/usr/bin/env python
# encoding: utf-8

"""
main.py
Created by dn on 2011-07-24.
Copyright (c) 2011 shubz. All rights reserved.
"""
import os
import re
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define, options

from eagles.handlers import *

# server running Options
define("debug", default=True, help="run the server mode Debug", type=bool)
define("port", default=8888, help="run on the given port", type=int)

# mongo server Options
define("mhost", default='192.168.11.10', help="hostname or IP address of the instance to connect to")
define("mport", default=8001, help="port number on which to connect", type=int)
define("mpool_size", default=50, help="The maximum size limit for the connection pool", type=int)

class Application(tornado.web.Application):
    def __init__ (self):
        settings = dict(
            debug = options.debug,
            template_path = os.path.join(os.path.dirname(__file__), "tpl"),
            static_url_prefix = "/static/",
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies = True,
            cookie_secret = "11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url = "/login",

            autoescape = None,
        )
        handlers = [
            (r"/", MainHandler),
            (re.escape(settings['static_url_prefix']) + r"(.*)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
        ]
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

