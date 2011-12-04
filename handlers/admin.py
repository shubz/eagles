# encoding: utf-8

import tornado 
import datetime
import uuid
import hashlib

from tornado import gen
from bson import ObjectId

from core.handler import AdminHandler
from core.session import session

class MainHandler(AdminHandler):

    @tornado.web.asynchronous
    @session
    def get(self):
        self.render("admin/index.html")

class LoginHandler(AdminHandler):

    @tornado.web.asynchronous
    @session
    def get(self):
        self.render("admin/login.html")

class ManagersHandler(AdminHandler):
    """后台用户的管理"""

    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        """管理员列表"""
        response,error = yield gen.Task(self.db.managers.find)
        self.render('admin/managers.html', managers=response[0])

    @tornado.web.asynchronous
    @gen.engine
    def post(self):
        """添加管理员"""
        email = self.get_argument('email')
        password = self.get_argument('password')
        password2 = self.get_argument('password2')
        if password != password2:
            errors = {'password2':"两次密码输入不一致"}
            self.render('admin/managers_new.html', email=email, errors=errors)
        else:
            salt = str(uuid.uuid1())[0:6]
            password = hashlib.md5(password+salt).hexdigest()
            ip = self.request.remote_ip
            response,error = yield gen.Task(self.db.managers.insert,{
                'email':email, 
                'password':password,
                'salt':salt,
                'created_time':datetime.datetime.now(),
                'last_login':datetime.datetime.now(),
                'last_ip':ip})
            self.redirect('/admin/managers')

class ManagersNewHandler(AdminHandler):
    """添加管理员"""
    @tornado.web.asynchronous
    def get(self):
        self.render('admin/managers_new.html', email='', errors={})
        
