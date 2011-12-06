# encoding: utf-8

import tornado 
import datetime
import uuid
import hashlib

from tornado import gen
from bson import ObjectId

from core.handler import AdminHandler
from core.session import session
from core.form import Form

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
        form = Form(self)
        form.get_email('email')
        form.get_two_password('password', 'password2')
        if form.errors:
            self.render('admin/managers_new.html', form=form)
        else:
            salt = str(uuid.uuid1())[0:6]
            password = hashlib.md5(form['password']+salt).hexdigest()
            ip = self.request.remote_ip
            response,error = yield gen.Task(self.db.managers.insert,{
                'email':form['email'], 
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
        form = Form(self)
        self.render('admin/managers_new.html', form=form)
        
