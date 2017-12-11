import unittest

import pickle

from src.models.API.API import API
from src.provider.FacebookProvider import FacebookProvider


class TestFbProvider(unittest.TestCase):
    
    provider = FacebookProvider()
    
    def test_getting_user(self):
        u = self.provider.get_user(API(0), '936799846374969')
        self.assertTrue(u.first_name == 'Mari')
        self.assertTrue(u.last_name == 'Koreneva')
        self.assertTrue(u.uid == '936799846374969')

        pickle.dump(u, open("fb_user", "wb"))
        u = pickle.load(open("fb_user", "rb"))
        print(u)