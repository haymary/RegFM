import vk

from src.exceptions.VKException import VKException
from src.models.API.API import API
from .Auth import Auth


class VKAuth(Auth):
    
    access_token = '53b495ac5e8e1ac22d0efac63c7df533d47250b67057e70b016e871602854c21be9c07ab08d7208b9667d'
    _api = None
    
    def __init__(self, access_token):
        self.access_token = access_token
        self.get_api()
    
    def get_api(self) -> API:
        if self._api is None:
            try:
                session = vk.Session(access_token=self.access_token)
                vk_api = vk.API(session)
                self._api = API(vk_api)
            except Exception as e:
                raise VKException(e)
        return self._api
