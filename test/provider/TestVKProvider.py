import unittest

import pickle

from src.auth.VKAuth import VKAuth
from src.provider.VKProvider import VKProvider


class TestVKProvider(unittest.TestCase):
    provider = VKProvider()
    
    def test_getting_users_data(self):
        api = VKAuth().get_api()
        u = self.provider.get_user(api, 1)
        # [{'first_name': 'Pavel', 'last_name': 'Durov', 'id': 1}]
        self.assertTrue(u.first_name == 'Павел')
        self.assertTrue(u.last_name == 'Дуров')
        self.assertTrue(u.uid == 1)