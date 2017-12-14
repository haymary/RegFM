import unittest

import pickle

from src.models.API.API import API
from src.provider.FacebookProvider import FacebookProvider


class TestFbProvider(unittest.TestCase):
    fb_acces_token = "EAACEdEose0cBAIfqaelrifSnXzIbatMn6dIZBiITZCl36O7bnF3b6JvkIhN9mgGXPORFIQWZCrZATFHccCxepjLNWmOCZAJAZCXhZC1XRbfCGzddzaod6F3gE51fanZAB7eCyI2ZAvZAh1DR2DmwfGaKbh7KSgHD8AAdQZAT5SFlZCjI9y3ShhWmUSg4ZBJsK1OAO8yJP6kZBMXlHyLgZDZD"
    
    def test_getting_user(self):
        u = self.provider = FacebookProvider(self.fb_acces_token).get_user()
        self.assertTrue(u.first_name == 'Mari')
        self.assertTrue(u.last_name == 'Koreneva')
        self.assertTrue(u.uid == '936799846374969')