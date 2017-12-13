import unittest

from src.analysis.Analyzer import Analyzer


class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = Analyzer()
        
    def test_getting_skills(self):
        skills = self.analyzer.analyze_skills(['hello', 'no'])
        for skill in skills:
            self.assertTrue(skill == 0)
            
    def test_for_right_words(self):
        words = ['it']
        skills = self.analyzer.analyze_skills(words)
        print(skills)
        self.assertTrue(skills.index(1) == 14)