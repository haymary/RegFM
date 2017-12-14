from typing import List

from src.helpers.DataManager import DataManager
from src.helpers.LanguageClassifier import detect_lang


class Analyzer:
    def __init__(self):
        self.work_skills = DataManager().work_skills
    
    def analyze_skills(self, words:List):
        skills = [0] * len(self.work_skills.get('skill_names').get('en'))
        for word in words:
            lang = detect_lang(word)
            for i, jobs in enumerate(self.work_skills.get('jobs').get(lang, [])):
                for job_name in jobs:
                    if job_name in word.lower():
                        # print(job_name)
                        skills[i] = skills[i] + 1
        return skills
