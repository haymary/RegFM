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
    def analyze(self, user: AUser):
        self.analyze_skills(user)
        self.analyze_interests(user)

    @abstractmethod
    def analyze_skills(self, user: AUser):
        pass

    @abstractmethod
    def analyze_interests(self, user: AUser):
        pass