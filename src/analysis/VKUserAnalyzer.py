import vk

from src.analysis.Analyzer import Analyzer
from src.models.user.VKUser import VKUser
from .AUserAnalyzer import AUserAnalyzer


class VKUserAnalyzer(AUserAnalyzer):
    def analyze_skills(self, user: VKUser):
        user_skills = user.jobs
        user_skills.extend(user.educations)
        user.skills_weights = Analyzer().analyze_skills(user.jobs)
        
    def analyze_interests(self, user: VKUser):
        user_groups = [g['name'] for g in user.groups]
        user_groups.extend(user.reposts_from)
        user_groups = list(set(user_groups))
        user_groups.extend(user.posts)
        int1 = Analyzer().analyze_skills(user_groups)
        user.interests_from_skills_weights = [i1 + i2 for i1, i2 in zip(int1, user.skills)]