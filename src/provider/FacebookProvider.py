import requests

from src.exceptions.FacebookException import FacebookException
from src.models.API.API import API
from src.models.user.FbUser import FbUser
from src.provider.AProvider import AProvider


class FacebookProvider(AProvider):
    _token = 'access_token=' \
             'EAACEdEose0cBAF6lOQvgbdZCt7c1sltBntcNGuZCjmZC4UZAlsF2rvoSKGEIlEVbd4YCSPxAYOgSSFkpPIpMeAaGtr85Ddrck6JeA8Hr0kpEuyobFUfP5MJjCOvZCkVUcQTfwPGCluz0a4ZAeBIi1jszy7d4vi3wVS7aB1rMVnMprYnd13WGX8yOlnjjOcrU9MtfM3MNcVHwZDZD'
    
    _request_base = 'https://graph.facebook.com/v2.11/'
    
    _fields = 'first_name,last_name,about,education,favorite_athletes,favorite_teams,inspirational_people,languages,' \
              'sports,work '
    
    _edges_names = ['albums', 'events', 'games', 'movies', 'music', 'television', 'books']
    
    def get_user(self, uid='me', access_token='') -> FbUser:
        # TODO: Delete for production
        if access_token != '':
            self._token = access_token
        try:
            request = self._request_base + \
                      uid + '?' + \
                      '&' + self._fields + \
                      '&' + self._token
            user = requests.get(request).json()

            if user.get('code') == 200: # Error validating access token
                return FbUser(user, *[self.search_edge(edge, uid) for edge in self._edges_names])
            message = ''
            if "type" in user:
                message = user.get("type") + ': '
            if "message" in user:
                message = message + user.get("message")
            raise FacebookException(message)
        except FacebookException as e:
            raise e
        except Exception as e:
            raise FacebookException(e)
        
    def search_edge(self, edge, uid='me'):
        try:
            request = self._request_base + \
                      uid + '/' + edge + '?' + self._token
            res = requests.get(request).json()
            result = (res.get('data', {}))
            if 'paging' in res:
                while 'next' in res.get('paging'):
                    res = requests.get(res.get('paging').get('next')).json()
                    result.extend(res.get('data', {}))
            return [r.get('name') for r in result]
        except Exception as _:
            return []
