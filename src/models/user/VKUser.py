from .AUser import AUser


class VKUser(AUser):
    def __init__(self, vk_user, wall, groups):
        super().__init__()
        vk_user = vk_user[0]
        self.uid = vk_user.get('uid')
        self.first_name = vk_user.get('first_name')
        self.last_name = vk_user.get('last_name')
        self.jobs = []
        jobs = vk_user.get('career', [])
        for job in jobs:
            self.jobs.append(job.get('position', ''))
        self.other_accounts = {'facebook': vk_user.get('facebook', ''),
                               'instagram': vk_user.get('instagram', '')}
        self.educations = []
        unis = vk_user.get('universities', [])
        for uni in unis:
            self.educations.append(uni.get('faculty_name', ''))
        self.groups = []
        for group in groups[1:]:
            self.groups.append({'name': group.get('name', ''), 'description': group.get('description', '')})
        self.posts = []
        posts = wall.get('wall', [])
        for post in posts[1:]:
            self.posts.append(post.get('text', ''))
        self.reposts_from = []
        reposts = wall.get('groups')
        for r in reposts:
            self.reposts_from.append(r.get('name', ''))
