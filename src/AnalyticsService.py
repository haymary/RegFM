from src.models.user.AUser import AUser


class AnalyticsService:
    
    def get_user_info(self, social_network: str, user_access_token: str) -> AUser:
        user = None
        if social_network is 'vk':
            # TODO
            pass
        else:
            # TODO
            pass
        return user
        
    def get_basic_user_info(self):
        # Retuns id, first name, last name, photo, job
        pass
    
    def get_user_skills(self):
        # Returns info of what he can do (according to jobs)
        pass
    
    def get_user_interests(self):
        # Returns what user could be intersted in on event (finding job/employee/colleagues  etc.)
        pass
        