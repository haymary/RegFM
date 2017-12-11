import vk

from src.exceptions.VKException import VKException
from src.models.API.API import API
from src.models.user.VKUser import VKUser
from .AProvider import AProvider


class VKProvider(AProvider):
    def get_user(self, api: API, uid=-1) -> VKUser:
        u_fields = ['photo_id', 'career', 'occupation', 'activities', 'interests',
                    'music', 'movies', 'tv', 'books', 'games',
                    'about', 'education', 'universities', 'connections']
        try:
            if uid < 0:
                user = api.get_api().users.get(fields=u_fields)
                groups = api.get_api().groups.get(extended=1, fields=['description'])
                wall = api.get_api().wall.get(extended=1)
            else:
                user = api.get_api().users.get(user_ids=uid, fields=u_fields)
                groups = api.get_api().groups.get(user_ids=uid, extended=1, fields=['description'])
                wall = api.get_api().wall.get(owner_id=uid, extended=1)
            return VKUser(user, wall, groups)
        except Exception as e:
            raise VKException(e)
