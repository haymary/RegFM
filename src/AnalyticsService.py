import time

from src.analysis.Analyzer import Analyzer
from src.analysis.EventAnalyzer import EventAnalyzer
from src.analysis.FbUserAnalyzer import FbUserAnalyzer
from src.analysis.VKUserAnalyzer import VKUserAnalyzer
from src.evaluation.Evaluator import Evaluator
from src.evaluation.EventEvaluator import EventEvaluator
from src.exceptions.WrongRequestException import WrongRequestException
from src.helpers.DataManager import DataManager
from src.models.user.AUser import AUser
from src.provider.FacebookProvider import FacebookProvider
from src.provider.VKProvider import VKProvider


class AnalyticsService:
    langs = ['ru', 'en']
    
    def __init__(self):
        self.social_network_analyzers = {
            'vk': VKUserAnalyzer(),
            'fb': FbUserAnalyzer()}
        self.evaluator = Evaluator()
        self.event_analyzer = EventAnalyzer()
        self.event_evaluator = EventEvaluator()
    
    # ------------- PUBLIC -------------
    
    def get_user_info(self, social_network: str, user_access_token: str, user_lang: str) -> dict:
        """
        Returns information about a user
        :param social_network: Name of social network to look for user ('vk' of 'fb')
        :param user_access_token: Access token for the network
        :param user_lang: code of the language of a user to translate info (only 'en' or 'ru')
        :return: Info about user in a form:
            {
                'social_network':{
                    'name',
                    'id'
                },
                'first_name',
                'last_name',
                'employment':{
                    'company',
                    'position'
                },
                'skills,
                'needs'
            }
        where:
            social_network['name']: name of social network ('vk' of 'fb'),
            social_network['id']: id of user,
            first_name: --,
            last_name: --,
            employment['company']: --,
            employment['position']: --,
            skills: user's skills detected by the system,
            needs: user's needs detected by the system
        """
        self._check_params(social_network, user_lang)
        
        user = self._get_user_info(social_network, user_access_token, user_lang)
        
        # To Return format
        result = {
            'social_network': {
                'name': social_network,
                'id': user.uid
            },
            "first_name": user.first_name,
            'last_name': user.last_name,
            'employment': user.employment,
            'skills': user.skills,
            'needs': user.skills
        }
        return result
    
    def get_user_friends_for_event(self, social_network: str, user_access_token: str, event_tags):
        """
        Returns user's friends who might be interested in event
        :param social_network: Name of social network to look for user ('vk' of 'fb')
        :param user_access_token: Access token for the network
        :param event_tags: List of tags for that event
        :return: Sorted list of user's friends, sorted by level of interest detected by system, in a form:
        A person is represented by dict:
            {
                'social_network':{
                    'name',
                    'id'
                },
                'first_name',
                'last_name',
                'how_interested'
            }
        where:
            social_network['name']: name of social network ('vk' of 'fb'),
            social_network['id']: id of user,
            first_name: --,
            last_name: --
            how_interested: system's score of particular user's interest in event
        """
        friends = self._get_user_friends(social_network, user_access_token, extended=True)
        analyzer = self.social_network_analyzers.get(social_network)
        for f in friends:
            analyzer.analyze(f)
    
        friends = self.event_evaluator.choose_people_for_event(friends, self.event_analyzer.get_event_types(event_tags))
        
        # To Return format
        result = [{
            'social_network': {
                'name': social_network,
                'id': friend.uid
            },
            'first_name': friend.first_name,
            'last_name': friend.last_name,
            'how_interested': friend.how_interested
        } for friend in friends]
        return result
    
    def get_meetings(self, social_network: str, user_access_token: str, user_lang: str, attenders):
        """
        Returns users which user might be interested to meet with reasons why
        :param social_network: Name of social network to look for user
        :param user_access_token: Access token for the network
        :param user_lang: code of the language of a user to translate info (only 'en' or 'ru')
        :param attenders: List of people who are going to attend the event
        A person(attender) is represented by dict:
            {
                'id',
                'job_position',
                'social_network':{
                    'name',
                    'id'
                }
            }
        where:
            id: id in reg.fm system,
            job_position: current job name,
            social_network['name']: name of social network,
            social_network['id']: id of user
        :return: List of dicts of a form:
            {
                'id',
                'reasons':{
                    'common_skills',
                    'interests',
                    'common_people'
                },
                'interest_score'
            }
        where:
            id: id in reg.fm system,
            reasons['common_skills']: list of common skills (List(str))
            reasons['interests']: list of common interests (List(str))
            reasons['common_people']: number of people they both know
        """
        self._check_params(social_network, user_lang)
        
        analyzer = self.social_network_analyzers.get(social_network)
        user = self._get_user_info(social_network, user_access_token, user_lang, analyzer)
        
        people_to_meet = []
        
        for attender in attenders:
            how_common = 0
            common_skills = []
            common_interests = []
            common_friends = []
            
            if attender.get('social_network', {}).get('name', '') == social_network:
                at = self._get_user_info(
                    social_network,
                    user_access_token,
                    user_lang,
                    analyzer,
                    attender.get('social_network').get('id'))
                # Common skills
                at_skill_weights = at.interests_from_skills_weights
                # Common interests
                intersection = list(set(user.interests).intersection(set(at.interests)))
                common_interests.extend(intersection)
                how_common += len(intersection)
                # Common people
                user_friends = self._get_user_friends(social_network, user_access_token)
                time.sleep(1)
                at_friends = self._get_user_friends(social_network, user_access_token, at.uid)
                u_friends_ids = [friend.get('uid') for friend in user_friends]
                a_friends_ids = [friend.get('uid') for friend in at_friends]
                common_friends = [friend for friend in user_friends
                                  if friend.get('uid') in set(u_friends_ids).intersection(set(a_friends_ids))]
                how_common += len(common_friends)
            else:
                
                at_skill_weights = DataManager().skills_weights_to_skills_weights(
                                      Analyzer().analyze_skills([attender.get('job_position', '')]),
                                      user_lang)
            
            at_skill_names = [s['name'] for s in at_skill_weights]
            
            for i, skill in enumerate(user.interests_from_skills_weights):
                if skill['name'] in at_skill_names:
                    how_common += skill['weight'] * at_skill_weights[at_skill_names.index(skill['name'])].get('weight')
                    common_skills.append(skill['name'])
            
            people_to_meet.append({
                'id': attender.get('id'),
                'reasons':{
                    'common_skills': common_skills,
                    'interests': common_interests,
                    'common_people': common_friends
                },
                'interest_score': how_common
            })
        return sorted(people_to_meet, key=lambda x: x['interest_score'], reverse=True)
        
    # ------------- PRIVATE -------------
    
    def _get_user_info(self, social_network, user_access_token, user_lang, analyzer=None, uid='me'):
        """
        Gets info abut user from social network and analyzes and evaluates results
        :param social_network: --
        :param user_access_token: --
        :param user_lang: --
        :param analyzer: AUserAnalyzer object
        :param uid: id of user in the social network
        """
        if analyzer is None:
            analyzer = self.social_network_analyzers.get(social_network)
        user = self._get_user_from_sn(social_network, user_access_token, uid)
        analyzer.analyze(user)
        self.evaluator.evaluate(user, user_lang)
        return user
    
    def _get_user_friends(self, social_network, user_access_token, uid='me', extended=False):
        """
        Gets friends of a specified user from a specified network
        :param social_network: --
        :param user_access_token: --
        :param uid: id of user in the social network
        :param extended: bool
            if True: program searches for the whole user profile and returns AUser instance for specified social network
            if False: only fields 'first_name', 'last_name' and 'id' are returned in dict with corresponding fields
        :return: AUser instance of dict
        """
        if extended:
            if social_network is 'vk':
                friends = VKProvider(access_token=user_access_token).get_user_friends_extended(uid)
            else:
                friends = FacebookProvider(access_token=user_access_token).get_user_friends_extended(uid)
        else:
            if social_network is 'vk':
                friends = VKProvider(access_token=user_access_token).get_user_friends(uid)
            else:
                friends = FacebookProvider(access_token=user_access_token).get_user_friends(uid)
        return friends
    
    def _check_params(self, social_network, user_lang):
        if social_network not in self.social_network_analyzers or user_lang not in self.langs:
            raise WrongRequestException('Wrong parameter value')
    
    def _get_user_from_sn(self, social_network, user_access_token, uid='me'):
        """
        Gets info about user from one of networks
        :param social_network: --
        :param user_access_token: --
        :param uid: --
        :return: AUser object
        """
        if social_network is 'vk':
            user = VKProvider(access_token=user_access_token).get_user(uid=uid)
        else:
            user = FacebookProvider(access_token=user_access_token).get_user(uid=uid)
        return user
