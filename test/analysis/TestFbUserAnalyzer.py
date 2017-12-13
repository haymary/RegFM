import unittest
from src.analysis.FbUserAnalyzer import FbUserAnalyzer
from data.users_test.Preloaded_Users import load_test_fb_user


class TestFbUserAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = FbUserAnalyzer()
        self.u = load_test_fb_user()
        
    def test_skill_analyzer_works(self):
        self.analyzer.analyze_skills(self.u)
        self.assertTrue(len(self.u.skills) > 0)
        
    def test_skill_analyzer(self):
        self.analyzer.analyze_skills(self.u)
        self.assertTrue(len(self.u.skills) > 0)
        self.assertTrue(self.u.skills[4] > 0)