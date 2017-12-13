from typing import List

import vk

from src.auth.VKAuth import VKAuth
from src.exceptions.VKException import VKException
from src.models.user.VKUser import VKUser
from .AProvider import AProvider


class VKProvider(AProvider):
    def __init__(self, access_token: str):
        super().__init__(access_token)
        self._api = VKAuth(access_token).get_api()
    
    def get_user(self, uid='me') -> VKUser:
        u_fields = ['photo_id', 'career', 'occupation', 'activities', 'interests',
                    'music', 'movies', 'tv', 'books', 'games',
                    'about', 'education', 'universities', 'connections']
        try:
            if uid is 'me':
                user = self._api.get_api().users.get(fields=u_fields)
                groups = self._api.get_api().groups.get(extended=1, fields=['description'])
                wall = self._api.get_api().wall.get(extended=1)
                career = user.get('career', [])
                employer = self._api.get_api().groups.getById(group_id=career[len(career) - 1].get('group_id'))
            else:
                user = self._api.get_api().users.get(user_ids=uid, fields=u_fields)
                groups = self._api.get_api().groups.get(user_ids=uid, extended=1, fields=['description'])
                wall = self._api.get_api().wall.get(owner_id=uid, extended=1)
                career = user.get('career', [])
                employer = self._api.get_api().groups\
                    .getById(user_ids=uid, group_id=career[len(career) - 1].get('group_id'))
            return VKUser(user, wall, groups, employer)
        except Exception as e:
            raise VKException(e)
    
    def get_user_friends(self, uid=-1) -> List[VKUser]:
        # TODO
        pass
