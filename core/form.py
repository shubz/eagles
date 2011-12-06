# encoding: utf-8

import re

class Form(object):
    '''表单处理类'''
    def __init__(self, handler):
        """初始化form数据"""
        self.handler = handler
        self._data = {}
        self._errors = {}

    @property
    def data(self):
        """收集的form数据"""
        return self._data

    @property
    def errors(self):
        """收集的错误"""
        return self._errors

    def __getitem__(self, key):
        """简化取值方式"""
        if self._data.has_key(key):
            return self._data[key]
        else:
            return ''

    def has_error(self, key):
        """检查是否存在某个key的错误"""
        if self._errors.has_key(key):
            return True
        else:
            return False

    def get_error(self, key):
        """获取某个错误的提示信息"""
        if self.has_error(key):
            return self.errors[key]
        else:
            return ''

    def add_data(self, key, value):
        """添加form数据"""
        self._data[key] = value

    def add_error(self, key, message):
        """添加错误"""
        self._errors[key] = message

    def get(self, key):
        """获取普通的参数"""
        value = self.handler.get_argument(key)
        self.add_data(key, value)
        return value

    def get_email(self, key):
        """获取email格式的参数"""
        email = self.get(key)
        pattern = "^[a-zA-Z0-9!#$%&\'*+\\/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&\'*+\\/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$"
        a = re.match(pattern, email)
        if a is None:
            self.add_error(key, 'Email格式错误')

    def get_two_password(self, key1, key2):
        """用于处理重复输入密码的情况"""
        password1 = self.get(key1)
        password2 = self.get(key2)
        if(password1 != password2):
            self.add_error(key2, '两次密码输入不一致')

