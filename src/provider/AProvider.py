from typing import List

from abc import ABC, abstractmethod

from src.models.API.API import API
from src.models.user.AUser import AUser


class AProvider(ABC):
    def __init__(self, access_token: str):
        self._access_token = access_token
    
    @abstractmethod
    def get_user(self, uid) -> AUser:
        pass

    @abstractmethod
    def get_user_friends(self, uid) -> List[dict]:
        pass

    @abstractmethod
    def get_user_friends_extended(self, uid) -> List[AUser]:
        pass
