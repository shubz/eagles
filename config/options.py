from tornado.options import define

# server running Options
define("debug", default=True, help="run the server mode Debug", type=bool)
define("port", default=8888, help="run on the given port", type=int)

# mongo server Options
define("mpool_id", default='eagles', help="unique id for this connection pool")
define("mhost", default='127.0.0.1', help="hostname or IP address of the instance to connect to")
define("mport", default=27017, help="port number on which to connect", type=int)
define("mmaxcached", default=10, help="maximum inactive cached connections for this pool. 0 for unlimited", type=int)
define("mmaxconnections", default=50, help="maximum open connections for this pool. 0 for unlimited", type=int)
define("mdbname", default='test', help="mongo database name")

