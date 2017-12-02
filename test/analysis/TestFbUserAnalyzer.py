import unittest
from src.models.API.API import API
from src.analysis.FbUserAnalyzer import FbUserAnalyzer
from src.provider.FacebookProvider import FacebookProvider


class TestFbUserAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = FbUserAnalyzer()
        provider = FacebookProvider()
        u = self.provider.get_user(API(0), '936799846374969')
        
    def test_skill_analyzer(self):
        # TODO
        pass
