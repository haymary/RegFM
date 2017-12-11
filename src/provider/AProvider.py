from abc import ABC, abstractmethod

from src.models.API.API import API
from src.models.user.AUser import AUser


class AProvider(ABC):
    @abstractmethod
    def get_user(self, uid, access_token: str) -> AUser:
        pass
