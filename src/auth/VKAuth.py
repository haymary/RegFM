import vk

from src.models.API.API import API
from .Auth import Auth


class VKAuth(Auth):
    def auth(self):
        pass
    
    access_token = '80023c6180023c6180023c6150805daf338800280023c61da0d229715958beeee683636'
    
    def __init__(self):
        pass
    
    def get_api(self) -> API:
        # session = vk.Session(access_token=self.access_token)
        session = vk.AuthSession(app_id='6263634', user_login='marikoreneva@gmail.com', user_password='5607Spaceman540031')
        vk_api = vk.API(session)
        a = API(vk_api)
        return a
