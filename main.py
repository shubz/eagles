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

from shubz.eagle.handlers import BaseHandler

# server running Options
define("debug", default=True, help="run the server mode Debug", type=bool)
define("port", default=8888, help="run on the given port", type=int)

class MainHandler(BaseHandler):
    def get(self):
        self.render("index.html", title="旧书楼")

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

