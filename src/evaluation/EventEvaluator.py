from typing import List
from src.models.user.AUser import AUser


class EventEvaluator:
    def choose_people_for_event(self, friends: List[AUser], event_categories: List[int]):
        for friend in friends:
            how_interested = 0
            for num, weight in enumerate(event_categories):
                how_interested += friend.skills_weights[num] * weight
            friend.how_interested = how_interested
        friends = sorted(friends, key=lambda x: x.how_interested, reverse=True)
        return [friend for friend in friends if friend.how_interested > 1]