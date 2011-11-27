from tornado.httpclient import AsyncHTTPClient
from tornado.testing import AsyncHTTPTestCase
from main import Application

class EaglesHTTPTest(AsyncHTTPTestCase):
    def get_app(self):
        return Application()

    def test_homepage(self):
        self.http_client.fetch(self.get_url('/'), self.stop)
        response = self.wait()
        print response
        
