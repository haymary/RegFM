import unittest

from src.auth.VKAuth import VKAuth
from src.provider.VKProvider import VKProvider


class TestVKProvider(unittest.TestCase):
    provider = VKProvider()
    
    def test_getting_users_data(self):
        api = VKAuth().get_api()
        u = self.provider.get_user(api)
        print(u)