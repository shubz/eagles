import re
import tornado.web

from settings import settings_dict as settings
from handlers import book,site,admin

routes = [
      (r"/", site.MainHandler),
      (r"/sess", site.SessHandler),
      (r"/books/new", book.NewHandler),

      (r"/admin", admin.MainHandler),
      (r"/admin/login", admin.LoginHandler),
      (r"/admin/managers", admin.ManagersHandler),
      (r"/admin/managers/new", admin.ManagersNewHandler),
      (re.escape(settings['static_url_prefix']) + r"(.*)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
]
