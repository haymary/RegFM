import unittest
from src.AnalyticsService import AnalyticsService

class TestAnalyticsService(unittest.TestCase):
    vk_acces_token = "cf6545c36443a4e988ce182452e968be64f45354507ee2395b9adab4ce95b653d3ab962b9160221498ed0"
    fb_acces_token = "EAACEdEose0cBAHne6p56xkZBPtfojkZBUlToKa1oEL4R0zg5RAiznH1jUnHrQ3ZCff4RbLhxZAPomv5FY1KE3vm4WTbb1gaczyzw8sML4TESr6z0WkQEH8534n1jhmQtVPZAagQ8B2UTYL71AgFibhZBOxtrWXZBylTD9TPdyXG6yWmjlkhXSJG8ZBVsvOw49uaxY7z8RAM0tAZDZD"
    analytics = AnalyticsService()
    
    # get_user_info
    
    def test_get_user_info_vk(self):
        user_info = self.analytics.get_user_info('vk', self.vk_acces_token, 'en')
        print(user_info)
        self.assertTrue(user_info.get('needs')[0].get('name') == 'IT & Software Development')
        
    def test_get_user_info_fb(self):
        user_info = self.analytics.get_user_info('fb', self.fb_acces_token, 'en')
        print(user_info)
        self.assertTrue(user_info.get('needs')[1].get('name') == 'Engineering')

    def test_get_user_info_vk_ru(self):
        user_info = self.analytics.get_user_info('vk', self.vk_acces_token, 'ru')
        print(user_info)
        self.assertTrue(user_info.get('needs')[0].get('name') == 'Разработка программного обеспечения и информационные технологии')

    def test_get_user_info_fb_ru(self):
        user_info = self.analytics.get_user_info('fb', self.fb_acces_token, 'ru')
        print(user_info)
        self.assertTrue(user_info.get('needs')[1].get('name') == 'Инженерия')
    
    # get_user_friends_for_event
    
    def test_get_user_friends_for_event_vk(self):
        friends = self.analytics.get_user_friends_for_event('vk', self.vk_acces_token, ['StartUp', "Developers", "Managers"])
        print(friends)
        
    def test_get_user_friends_for_event_fb(self):
        friends = self.analytics.get_user_friends_for_event('fb', self.fb_acces_token, ['StartUp', "Developers", "Managers"])
        print(friends)