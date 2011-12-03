# encoding: utf-8

import tornado 

from tornado import gen
from bson import ObjectId

from core.handler import BaseHandler
from core.session import session

class MainHandler(BaseHandler):

    @tornado.web.asynchronous
    @session
    def get(self):
        self.session['test'] = 'wwwwww'
        self.render("site/index.html")

class SessHandler(BaseHandler):

    @tornado.web.asynchronous
    @session
    def get(self):
        if self.session['test']:
            self.write(self.session['test'])
        self.finish()

        
