from abc import ABC, abstractmethod
from src.models.user.AUser import AUser


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
    def analyze(self,  user: AUser):
        pass
    
    