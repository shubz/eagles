# encoding: utf-8

from tornado.options import options
from pymongo import Connection
from bson import ObjectId

class BaseModel(object):
    '''数据基类'''

    @property
    def conn(self):
        """自动创建连接"""
        if not hasattr(self, '_db'):
            self._db = Connection(options.mhost, options.mport, options.mpool_size)
        return self._db

    @property
    def collection_name(self):
        """数据集名称"""
        return ''

    @property
    def db(self):
        """默认数据集"""
        return self.conn.test[self.collection_name]

class Book(BaseModel):
    '''作品信息'''

    @property
    def collection_name(self):
        """对应的数据集名称"""
        return 'books'

    def find(self, id):
        """作品详细信息"""
        book = self.db.find_one({'_id': ObjectId(id)})
        return book

    def find_all(self, page_size, page=1, order='view_count', desc=True):
        """全部图书，默认返回基于阅读量排序的前20项"""
        books = self.db.find()
        return books
