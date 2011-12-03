# encoding: utf-8

import os
import options

from tornado.options import options
from core.session import FileEngine

settings_dict = dict(debug = options.debug,
        template_path = os.path.join(os.path.dirname(__file__), "../tpl"),
        static_url_prefix = "/static/",
        static_path = os.path.join(os.path.dirname(__file__), "../static"),
        xsrf_cookies = True,
        cookie_secret = "b23aadc7b8c0dbc5a9b38341944c3998b23aadc7b8",
        login_url = "/login",
        autoescape = None,
        session_engine = FileEngine(session_dir = './sessions'),
        session_timeout = 20*60, #20分钟
        session_time_key = '___timeout___', #内部记录session生成时间的key
        cookie_session_key = 'session_id', #cookie中记录session id的key

)
