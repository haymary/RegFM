from typing import List

import requests

from src.exceptions.FacebookException import FacebookException
from src.models.API.API import API
from src.models.user.FbUser import FbUser
from src.provider.AProvider import AProvider


class FacebookProvider(AProvider):

    _request_base = 'https://graph.facebook.com/v2.11/'
    
    _fields = 'first_name,last_name,about,education,favorite_athletes,favorite_teams,inspirational_people,languages,' \
              'sports,work'
    
    _edges_names = ['albums', 'events', 'games', 'movies', 'music', 'television', 'books']

    # ------------- PUBLIC -------------

    def get_user(self, uid='me') -> FbUser:
        try:
            request = f'{self._request_base}{uid}?fields={self._fields}&access_token={self._access_token}'
            user = requests.get(request).json()

            if 'error' in user:
                message = user.get('error').get("type", 'FacebookError') + ': '
                message = message + user.get('error').get("message", '')
                raise FacebookException(message)
            edges = [self._search_edge(edge, uid) for edge in self._edges_names]
            return FbUser(user, *edges)
        except FacebookException as e:
            raise e
        except Exception as e:
            raise FacebookException(e)

    def get_user_friends(self, uid='me'):
        """
        Returns friends in list of a form:
        [{
            "first_name": "João",
            "last_name": "Fernandes",
            "uid": "10153880234320990"
        }, ...]
        :param uid: user id
        :return: list of dicts
        """
        try:
            return [{
                "uid": friend.get("uid"),
                "first_name": friend.get("name", '').split(' ')[0],
                "last_name": friend.get("name", '').split(' ')[-1] if len(list(friend.get("name", ''))) > 1 else ''
            } for friend in self._get_user_friends(uid)]
        except Exception as e:
            raise FacebookException(e)
    
    def get_user_friends_extended(self, uid) -> List[FbUser]:
        try:
            return [self.get_user(friend.get('id')) for friend in self._get_user_friends(uid)]
        except Exception as e:
            raise FacebookException(e)
        
    # ------------- PRIVATE -------------

    def _search_edge(self, edge, uid='me'):
        result = self._search_edge_raw(edge, uid='me')
        return [r.get('name') for r in result]

    def _search_edge_raw(self, edge, uid='me'):
        request = f'{self._request_base}{uid}/{edge}?access_token={self._access_token}'
        res = requests.get(request).json()
        result = (res.get('data', {}))
        if 'paging' in res:
            while 'next' in res.get('paging'):
                res = requests.get(res.get('paging').get('next')).json()
                result.extend(res.get('data', {}))
        return result

    def _get_user_friends(self, uid='me'):
        """
        Returns friends in list of a form:
        [{
            "name": "João Fernandes",
            "uid": "10153880234320990"
        },
        ...]
        :param uid: user id
        :return: list of dicts
        """
        friends = self._search_edge_raw('friends', uid)
        return friends