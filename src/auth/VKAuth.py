import vk

from src.exceptions.VKException import VKException
from src.models.API.API import API
from .Auth import Auth


class VKAuth(Auth):
    
    access_token = '80023c6180023c6180023c6150805daf338800280023c61da0d229715958beeee683636'
    _api = None
    
    def __init__(self):
        pass
    
    def get_api(self) -> API:
        if self._api is None:
            try:
                # session = vk.Session(access_token=self.access_token)
                session = vk.AuthSession(app_id='6263634', user_login='marikoreneva@gmail.com', user_password='5607Spaceman540031')
                vk_api = vk.API(session)
                self._api = API(vk_api)
            except Exception as e:
                raise VKException(e)
        return self._api
