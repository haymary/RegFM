import pandas as pd
import pickle
import os

from src.helpers.Paths import Paths


class DataManager:
    paths = ''
    
    work_skills = {}
    user_lnags = ['en', 'ru']
    
    def __init__(self):
        self._basepath = os.path.dirname(__file__)
        if len(self.work_skills.keys()) == 0:
            self.paths = Paths()
            self._import_tags_tables()
    
    def _import_tags_tables(self):
        """Loads lists of tags of different categories.
        """
        # EN
        work_skills_en = self._get_dict(self.paths.work_skills_en)
        work_skills_ru = self._get_dict(self.paths.work_skills_ru)
        self.work_skills = {
            "skill_names": {
                "en": list(work_skills_en.keys()),
                "ru": list(work_skills_ru.keys())
            },
            "jobs": {
                "en": list(work_skills_en.values()),
                "ru": list(work_skills_ru.values())
            }
        }
    
    def _get_dict(self, path):
        table = pd.read_csv(
            self._get_path(path), skip_blank_lines=True, keep_default_na=False, dtype=str, error_bad_lines=False)
        res_dict = {}
        for col in table.columns:
            s = set(table[col])
            if '' in s:
                s.remove('')
            res_dict[col] = s
        return res_dict
    
    def _get_path(self, path):
        return os.path.abspath(os.path.join(self._basepath, "..", "..", path))
