# encoding: utf-8

import tornado 

from tornado import gen
from bson import ObjectId

from core.handler import BaseHandler

class MainHandler(BaseHandler):

    @tornado.web.asynchronous
    def get(self):
        self.render("site/index.html")
