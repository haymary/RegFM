import unittest

from src.helpers.DataManager import DataManager


class TestDataMenager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
    
    def test_skills_imported(self):
        self.assertTrue(len(self.data_manager.work_skills) is not {})
    #
    # Test imported right
    #
    def test_skills_created_right(self):
        print(self.data_manager.work_skills)
        self.assertTrue('skill_names' in self.data_manager.work_skills.keys())
        self.assertTrue('jobs' in self.data_manager.work_skills.keys())

    def test_skills_imported_right(self):
        self.assertTrue('Biotech, R&D & Science' in self.data_manager.work_skills.get('skill_names').get('en'))
        self.assertTrue('Compliance' in self.data_manager.work_skills.get('jobs').get('en')[0])
