# encoding: utf-8

import tornado 

from tornado import gen
from bson import ObjectId

from core.handler import BaseHandler

class MainHandler(BaseHandler):

    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        response,error = yield gen.Task(self.db.books.find_one,{'_id': ObjectId('234234234')})
        if error['error']:
            raise tornado.web.HTTPError(500)
        book = response[0]
        self.render("index.html", title=book['name'], content=book['intro'])
