from .AUser import AUser


class VKUser(AUser):
    def __init__(self, user, wall, groups):
        super().__init__()
        user = user[0]
        
        # Personal
        self.uid = user.get('uid')
        self.first_name = user.get('first_name')
        self.last_name = user.get('last_name')
        self.other_accounts = {'facebook': user.get('facebook', ''),
                               'instagram': user.get('instagram', '')}
        # Skills
        self.jobs = [job.get('position', '') for job in user.get('career', [])]
        self.educations = [uni.get('faculty_name', '') for uni in user.get('universities', [])]
        
        # Interests
        self.groups = [{'name': group.get('name', ''), 'description': group.get('description', '')} for group in
                       groups[1:]]
        self.posts = [post.get('text', '') for post in wall.get('wall', [])[1:]]
        self.reposts_from = [r.get('name', '') for r in wall.get('groups', [])]
        
        career = user.get('career', [])
        if len(career) == 0:
            employer = ''
        else:
            employer = career[-1].get('company', '')
        if len(self.jobs) > 0:
            self.employment = {
                'company': employer,
                'position': self.jobs[len(self.jobs) - 1]
            }