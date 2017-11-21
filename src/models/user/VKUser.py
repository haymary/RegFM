from .AUser import AUser


class VKUser(AUser):
    def __init__(self, vk_user, wall, groups):
        super().__init__()
        vk_user = vk_user[0]
        self.uid = vk_user.get('uid')
        self.first_name = vk_user.get('first_name')
        self.last_name = vk_user.get('last_name')
        self.jobs = [job.get('position', '') for job in vk_user.get('career', [])]
        self.other_accounts = {'facebook': vk_user.get('facebook', ''),
                               'instagram': vk_user.get('instagram', '')}
        self.educations = [uni.get('faculty_name', '') for uni in vk_user.get('universities', [])]
        self.groups = [{'name': group.get('name', ''), 'description': group.get('description', '')} for group in
                       groups[1:]]
        self.posts = [post.get('text', '') for post in wall.get('wall', [])[1:]]
        self.reposts_from = [r.get('name', '') for r in wall.get('groups')]
