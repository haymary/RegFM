from .AUser import AUser


class FbUser(AUser):
    def __init__(self, user, albums, events, games, movies, music, television, books):
        super().__init__()
        self.education = [school.get('school', {}).get('name', '') for school in user.get('education', {})]
        self.languages = [lang.get('name', '') for lang in user.get('languages')]
        self.jobs = [job.get('position', {}).get('name', '') for job in user.get('work', {})]
        self.uid = user.get('id')
        self.first_name = user.get('first_name', '')
        self.last_name = user.get('last_name', '')
        self.about = user.get('about', '')
        self.favorite_athletes = [a.get('name', '') for a in user.get('favorite_athletes', {})]
        self.favorite_teams = [team.get('name', '') for team in user.get('favorite_teams', {})]
        self.inspirational_people = [p.get('name', '') for p in user.get('inspirational_people', {})]
        self.sports = [s.get('name', '') for s in user.get('sports', {})]
        self.albums = albums
        self.events = events
        self.games = games
        self.movies = movies
        self.music = music
        self.television = television
        self.books = books
