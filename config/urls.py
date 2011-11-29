import re
import tornado.web

from settings import settings_dict as settings
from handlers.book import *

routes = [
      (r"/", MainHandler),
      (re.escape(settings['static_url_prefix']) + r"(.*)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
]
