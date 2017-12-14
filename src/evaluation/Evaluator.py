from src.models.user.AUser import AUser
from src.helpers.DataManager import DataManager


class Evaluator(object):
    
    def evaluate(self, user: AUser, lang):
        dm = DataManager()
        user.skills_weights = dm.skills_weights_to_skills_weights(user.skills_weights, lang)
        user.interests_from_skills_weights = \
            dm.skills_weights_to_skills_weights(user.interests_from_skills_weights, lang)

        user.skills = sorted(user.skills_weights, key=lambda x: x['weight'], reverse=True)
        user.interests_from_skills = sorted(user.interests_from_skills_weights, key=lambda x: x['weight'], reverse=True)