from tornado.options import define

# server running Options
define("debug", default=True, help="run the server mode Debug", type=bool)
define("port", default=8888, help="run on the given port", type=int)

# mongo server Options
define("mhost", default='192.168.11.10', help="hostname or IP address of the instance to connect to")
define("mport", default=8001, help="port number on which to connect", type=int)
define("mpool_size", default=50, help="The maximum size limit for the connection pool", type=int)

