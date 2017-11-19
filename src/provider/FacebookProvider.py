

from src.models.API.API import API
from src.models.user.AUser import AUser
from src.provider.AProvider import AProvider


class FacebookProvider(AProvider):
    def get_user(self, api: API) -> AUser:
        pass