import unittest
from src.AnalyticsService import AnalyticsService


class TestAnalyticsService(unittest.TestCase):
    vk_acces_token = "cf6545c36443a4e988ce182452e968be64f45354507ee2395b9adab4ce95b653d3ab962b9160221498ed0"
    fb_acces_token = "EAACEdEose0cBAFErsuXLFpAvtOSPf5S3ORGJ9iqu6ez6jN3OoIcBxgvEQ1cG2bVwRZCitiEbADT0Ty9pR7WpmZBuFuDCQZCk4wNxDWZCDhYF48ZBR3PhTdu2jAt9zux5dqvBQt1f7JAlWJu9OzmnAUaa8fDtN8iUy6lxkFrMEVTkr4UcZC1ysewaE3ZAZAoo7QuAPuAtSFBQ1wZDZD"
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
        self.assertTrue(
            user_info.get('needs')[0].get('name') == 'Разработка программного обеспечения и информационные технологии')
    
    def test_get_user_info_fb_ru(self):
        user_info = self.analytics.get_user_info('fb', self.fb_acces_token, 'ru')
        print(user_info)
        self.assertTrue(user_info.get('needs')[1].get('name') == 'Инженерия')
    
    # get_user_friends_for_event
    
    def test_get_user_friends_for_event_vk(self):
        friends = self.analytics.get_user_friends_for_event('vk', self.vk_acces_token,
                                                            ['StartUp', "Developers", "Managers"])
        print(friends)
        self.assertTrue(len(friends) > 0)
    
    def test_get_user_friends_for_event_fb(self):
        friends = self.analytics.get_user_friends_for_event('fb', self.fb_acces_token,
                                                            ['StartUp', "Developers", "Managers"])
        print(friends)
        self.assertTrue(len(friends) > 0)
    
    # get_meetings
    
    def test_get_meetings_vk(self):
        people = [
            {
                'id': 0,
                'job_position': 'software developer',
                'social_network': {
                    'name': 'fb',
                    'id': '906351386055094'
                }
            }, {
                'id': 1,
                'job_position': 'software developer',
                'social_network': {
                    'name': 'vk',
                    'id': '17611433'
                }
            }, {
                'id': 3,
                'job_position': 'software developer',
                'social_network': {
                    'name': 'vk',
                    'id': '215524314'
                }
            }
        ]
        meetings = self.analytics.get_meetings('vk', self.vk_acces_token, 'en', people)
        self.assertTrue(len(meetings) > 0)
        
    def test_get_meetings_fb(self):
        people = [
            {
                'id': 0,
                'job_position': 'software developer',
                'social_network': {
                    'name': 'fb',
                    'id': 'me'
                }
            }, {
                'id': 1,
                'job_position': 'software developer',
                'social_network': {
                    'name': 'vk',
                    'id': '17611433'
                }
            }, {
                'id': 3,
                'job_position': 'artist',
                'social_network': {
                    'name': 'fb',
                    'id': '10155138239048996'
                }
            }
        ]
        meetings = self.analytics.get_meetings('fb', self.fb_acces_token, 'en', people)
        self.assertTrue(len(meetings) > 0)
