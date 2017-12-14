from typing import List

from src.helpers.DataManager import DataManager
from src.helpers.LanguageClassifier import detect_lang


class Analyzer:
    def __init__(self):
        self.work_skills = DataManager().work_skills
    
    def analyze_skills(self, words: List[str]):
        """
        Looks for appearance of words from tables of words which correspond to specific professional fields(or skill)
        in supplied list of words and counts the number of appearances of words of each category(weights) in the list.
        :param words: list of strings
        :return: List of length equal to the number of professional fields categories in the tables: i-th cell
        corresponds to i-th category and value of i-th cell is the number of words of that category found in the
        supplied list.
        """
        skills = [0] * len(self.work_skills.get('skill_names').get('en'))
        for word in words:
            lang = detect_lang(word)
            for i, jobs in enumerate(self.work_skills.get('jobs').get(lang, [])):
                for job_name in jobs:
                    if job_name in word.lower():
                        skills[i] = skills[i] + 1
        return skills
