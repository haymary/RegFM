from typing import List

import time

from src.auth.VKAuth import VKAuth
from src.exceptions.VKException import VKException
from src.models.user.VKUser import VKUser
from .AProvider import AProvider


class VKProvider(AProvider):
    def __init__(self, access_token: str):
        super().__init__(access_token)
        self._api = VKAuth(access_token).get_api()
    
    # ------------- PUBLIC -------------
    
    def get_user(self, uid='me') -> VKUser:
        u_fields = ['photo_id', 'career', 'occupation', 'activities', 'interests',
                    'music', 'movies', 'tv', 'books', 'games',
                    'about', 'education', 'universities', 'connections']
        try:
            if uid is 'me':
                user = self._api.get_api().users.get(fields=u_fields)
                groups = self._api.get_api().groups.get(extended=1, fields=['description'])
                wall = self._api.get_api().wall.get(extended=1)
            else:
                user = self._api.get_api().users.get(user_ids=uid, fields=u_fields)
                if len(user) == 0:
                    raise VKException("User is empty")
                groups = self._api.get_api().groups.get(user_ids=uid, extended=1, fields=['description'])
                wall = self._api.get_api().wall.get(owner_id=uid, extended=1)
            return VKUser(user, wall, groups)
        except VKException as e:
            raise e
        except Exception as e:
            raise VKException(e)
    
    def get_user_friends(self, uid='me'):
        try:
            return [{
                'uid': user.get('uid'),
                'first_name': user.get('first_name', ''),
                'last_name': user.get('last_name', '')
            } for user in self._get_user_friends(uid)]
        except Exception as e:
            raise VKException(e)
    
    def get_user_friends_extended(self, uid) -> List[VKUser]:
        friends = []
        for friend in self._get_user_friends(uid):
            friends.append(self.get_user(friend.get('uid')))
            time.sleep(1)
        return friends
    
    def get_all_friends(self):
        try:
            u_fields = ['photo_id', 'career', 'occupation', 'activities', 'interests',
                        'music', 'movies', 'tv', 'books', 'games',
                        'about', 'education', 'universities', 'connections']
            friends = self._api.get_api().friends.get(fields=u_fields)
            return [VKUser([friend], {}, []) for friend in friends]
        except Exception as e:
            raise VKException(e)

    # ------------- PRIVATE -------------
    
    def _get_user_friends(self, uid):
        u_fields = ['first_name', 'last_name']
        if uid is 'me':
            friends = self._api.get_api().friends.get(fields=u_fields)
        else:
            friends = self._api.get_api().friends.get(user_id=uid, fields=u_fields)
        return friends
    
    
