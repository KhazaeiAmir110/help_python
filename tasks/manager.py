class UserManager:
    users = list()



    def create(self,*args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.users.append(self)

    def append(self, user: 'User'):
        self.users.append(user)

    def delete(self, *args, **kwargs):
        for _user in self.users:
            print(vars(_user))
            for key, value in kwargs.items():
                if getattr(_user, key) == value:
                    self.users.remove(_user)
                    # return vars(_user)

    def filter(self,*args, **kwargs):
        _result = list()
        for _user in self.users:
            for key, value in kwargs.items():
                if getattr(_user, key) == value:
                    _result.append(_user)

        return _result

    def get(self, **kwargs):
        get_list = list()
        for _user in self.users:
            for key, value in kwargs.items():
                if getattr(_user, key) == value:
                    get_list.append(_user)
        if len(get_list) == 0:
            return None
        elif len(get_list) > 1:
            return ValueError("ERROR : User More than one")
        else:
            return vars(get_list[0])

    def list(self):
        for _ in self.users:
            print(vars(_))

class User:
    objects = UserManager()

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.objects.append(self)
