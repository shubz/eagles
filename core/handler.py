import tornado.web
import asyncmongo

from tornado.options import options

class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        if not hasattr(self, '_db'):
            self._db = asyncmongo.Client(
                    pool_id=options.mpool_id, 
                    host=options.mhost, 
                    port=options.mport, 
                    maxcached=options.mmaxcached, 
                    maxconnections=options.mmaxconnections, 
                    dbname=options.mdbname)
        return self._db

    def get_current_user(self):
        return self.get_secure_cookie("user")

