

class AUser(object):
    def __init__(self):
        self.last_name = None
        self.first_name = None

    def __repr__(self):
        return "User: %s %s" % (self.first_name, self.last_name)


