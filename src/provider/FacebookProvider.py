import requests

from src.models.API.API import API
from src.models.user.FbUser import FbUser
from src.provider.AProvider import AProvider


class FacebookProvider(AProvider):
    _token = 'access_token=' \
             'EAACEdEose0cBAIZAbo4SoHXYioDYseutSD4cUJSKWZBRqCntiswyvDmLkCNzFaF56lJ56s6MHY1RWD9PixZAdQJZBC6dBycCZAZAmSR09o5l9w3dssYoVZCdZCBVGcAAzQSaQ40npsiprWhkZC5ffEUq1TUIewITuJx2eQXHvd38J2mb0oa11E0IMdGZCZBAKHDW0xhQwZCQnzKZCbQZDZD'
    
    _request_base = 'https://graph.facebook.com/v2.11/'
    
    def get_user(self, api: API, uid='me') -> FbUser:
        fields = ['first_name', 'last_name', 'about', 'education',
                  'favorite_athletes', 'favorite_teams', 'inspirational_people',
                  'languages', 'sports', 'work']
        
        fields_s = 'fields=%s' % self._fields_to_str(fields)
        
        request = self._request_base + \
                  uid + '?' + \
                  '&' + fields_s + \
                  '&' + self._token
        
        user = requests.get(request).json()
        
        edges_names = ['albums', 'events', 'games', 'movies', 'music', 'television', 'books']
        
        return FbUser(user, *[self.search_edge(edge) for edge in edges_names])
    
    def search_edge(self, edge, uid='me'):
        request = self._request_base + \
                  uid + '/' + edge + '?' + self._token
        res = requests.get(request).json()
        result = (res.get('data', {}))
        if 'paging' in res:
            while 'next' in res.get('paging'):
                res = requests.get(res.get('paging').get('next')).json()
                result.extend(res.get('data', {}))
        return [r.get('name') for r in result]
    
    def _fields_to_str(self, fields):
        str = ''
        for f in fields:
            str += f + ','
        return str[:len(str) - 1]
