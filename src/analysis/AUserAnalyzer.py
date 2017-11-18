from abc import ABC, abstractmethod

from src.models.API.API import API


class AUserAnalyzer(ABC):
    """
    Module automatically finds:
     - User's name
     - Company
     - Job
     - Photo
     Also derives:
     - User's skills
     - User's needs
    """
    @abstractmethod
    def analyze(self, api: API, user_id):
        pass
    
    