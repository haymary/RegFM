import unittest
from src.auth.VKAuth import VKAuth
from src.provider.VKProvider import VKProvider


class TestVKAuth(unittest.TestCase):
    provider = VKProvider()
    auth = VKAuth()
    
    def test_auth(self):
        api = VKAuth().get_api()
        self.assertTrue(api is not None)