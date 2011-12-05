# encoding: utf-8

import pickle
import time
import hashlib
import uuid
import os

class BaseEngine(object):
    """session存储引擎基类，实现其他存储方式只需继承本类并实现对应的方法"""
    def read(self, session_id):
        """读取session内容"""
        pass
    def write(self, session_id, data):
        """写入session内容"""
        pass
    def delete(self, session_id):
        """删除session内容"""
        pass

class FileEngine(BaseEngine):
    """使用文件存储session"""
    def __init__(self, *args, **kwargs):
        self.session_dir = kwargs['session_dir']

    def get_session_path(self, session_id):
        return  os.path.join(self.session_dir, session_id)

    def read(self, session_id):
        """读取session内容"""
        try:
            session_path = self.get_session_path(session_id)
            data = pickle.load(open(session_path, 'r'))
            if isinstance(data, dict):
                return data
            else:
                return None
        except:
            return None

    def write(self, session_id, data):
        """写入session内容"""
        session_path = self.get_session_path(session_id)
        pickle.dump(data, open(session_path, 'w') )

    def delete(self, session_id):
        session_path = self.get_session_path(session_id)
        os.remove(session_path)
         
class SessionManager(dict):
    def __init__(self, engine=None, timeout=20*60, time_key='___timeout___'):
        self.changed = False
        self.engine = engine #使用的存储引擎
        self.timeout = timeout #超时时间
        self.time_key = time_key #存储session创建时间的key

    def load(self, session_id=None):
        '''加载session数据'''
        if not session_id: #session id异常
            return False
        data = self.engine.read(session_id)
        if not data:  #数据异常
            return False
        self.session_id = session_id
        super(SessionManager, self).update(data)
        if self.is_timeout():
            self.engine.delete(self.session_id) #超时清除旧session
            return False
        return True

    def is_timeout(self):
        """检查是否超时"""
        that_time = super(SessionManager, self).__getitem__(self.time_key)
        now = time.time()
        if type(now) == type(that_time):
            return time.time() - that_time > self.timeout #现在时间-过去时间>超时时间 即过期
        else:
            return False

    def new(self):
        '''创建一个新的空session'''
        self.changed = True
        self.session_id = self.new_session_id()
        super(SessionManager, self).clear()
        super(SessionManager, self).__setitem__(self.time_key, time.time())

    def new_session_id(self):
        '''生成一个新的session id'''
        base = hashlib.md5(str(uuid.uuid1()))
        return base.hexdigest()

    def __missing__(self, key):
        return None

    def __setitem__(self, key, value):
        '''设置session项'''
        self.changed = True
        return super(SessionManager, self).__setitem__(key, value)

    def save(self):
        '''保存session, 只有数据被更改时才写入'''
        if self.changed:
            self.engine.write(self.session_id, super(SessionManager, self).copy())

def session(method):
    def wrapper(self, *args, **kwargs):
        session_engine = self.application.settings['session_engine']
        timeout = self.application.settings['session_timeout']
        time_key = self.application.settings['session_time_key']
        cookie_session_key = self.application.settings['cookie_session_key']

        self.session = SessionManager(session_engine, timeout, time_key)
        session_id = self.get_secure_cookie(cookie_session_key)
        if not self.session.load(session_id): #session不存在或超时则创建一个新的空session
            self.session.new()
        self.set_secure_cookie(cookie_session_key, self.session.session_id)

        method(self, *args, **kwargs)
        self.session.save()
    return wrapper
