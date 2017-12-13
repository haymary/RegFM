from src.analysis.VKUserAnalyzer import VKUserAnalyzer
from data.users_test.Preloaded_Users import load_test_vk_user

import unittest


class TestVKAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = VKUserAnalyzer()
        self.u = load_test_vk_user()

    def test_skill_analyzer_works(self):
        self.analyzer.analyze_skills(self.u)
        self.assertTrue(len(self.u.skills) > 0)

    def test_skill_analyzer(self):
        self.analyzer.analyze_skills(self.u)
        self.assertTrue(self.u.skills[6] > 0)