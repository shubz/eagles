# encoding: utf-8

import tornado 

from eagles.models import *

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        book = Book().find('4ed0b5b1421aa94ed5000000')
        self.render("index.html", title=book['name'], content=book['intro'])
