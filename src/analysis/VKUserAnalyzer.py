import vk

from src.models.API.API import API
from src.models.user.AUser import AUser
from src.models.user.VKUser import VKUser
from .AUserAnalyzer import AUserAnalyzer


class VKUserAnalyzer(AUserAnalyzer):
    def analyze(self, api: API, user_id):
        # TODO
        pass
