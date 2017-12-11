class FacebookException(Exception):
    def __init__(self, m=''):
        self.message = m