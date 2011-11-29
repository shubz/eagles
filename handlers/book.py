# encoding: utf-8

import tornado 

from tornado import gen
from bson import ObjectId

from core.handler import BaseHandler

class MainHandler(BaseHandler):

    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        response,error = yield gen.Task(self.db.books.find_one,{'_id': ObjectId('4ed0b5b1421aa94ed5000000')})
        if error['error']:
            raise tornado.web.HTTPError(500)
        print response
        book = response[0]
        self.render("index.html", title='name', content='intro')

class NewHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render('book/new.html')
        
