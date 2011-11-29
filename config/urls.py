import re
import tornado.web

from settings import settings_dict as settings
from handlers import book,site

routes = [
      (r"/", site.MainHandler),
      (r"/books/new", book.NewHandler),
      (re.escape(settings['static_url_prefix']) + r"(.*)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
]
