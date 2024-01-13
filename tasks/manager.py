class UserManager:
    users = list()



    def create(self,*args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.users.append(self)

    def append(self, user: 'User'):
        self.users.append(user)


class User:
    objects = UserManager()

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.objects.append(self)
