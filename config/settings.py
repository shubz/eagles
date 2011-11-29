import os
import options

from tornado.options import options

settings_dict = dict(debug = options.debug,
      template_path = os.path.join(os.path.dirname(__file__), "tpl"),
      static_url_prefix = "/static/",
      static_path = os.path.join(os.path.dirname(__file__), "static"),
      xsrf_cookies = True,
      cookie_secret = "11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
      login_url = "/login",
      autoescape = None,
)
