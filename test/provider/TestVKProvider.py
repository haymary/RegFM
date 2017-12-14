import unittest

import pickle

from src.auth.VKAuth import VKAuth
from src.provider.VKProvider import VKProvider


class TestVKProvider(unittest.TestCase):
    vk_access_token = "cf6545c36443a4e988ce182452e968be64f45354507ee2395b9adab4ce95b653d3ab962b9160221498ed0"
    
    def test_getting_users_data(self):
        u = VKProvider(access_token=self.vk_access_token).get_user(uid=1)
        # [{'first_name': 'Pavel', 'last_name': 'Durov', 'id': 1}]
        self.assertTrue(u.first_name == 'Павел')
        self.assertTrue(u.last_name == 'Дуров')
        self.assertTrue(u.uid == 1)
