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


    def update(self, *args, **kwargs):
        for _user in self.users:
            for key, value in kwargs.items():
                if getattr(_user, key) == value:
                    setattr(_user,key, value)
                    # self.users.remove(_user)
                    # User.objects.create(*args, **kwargs)
                    # return True


    def list(self):
        for _ in self.users:
            print(vars(_))

class User:
    objects = UserManager()

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.objects.append(self)


if __name__ == '__main__':
    user1 = User(name='ali', age=2)

    user2 = User(name='ali2', age=2)
    # User.objects.get(name='ali')
    # User.objects.filter(name='a', age=2)
    us = User.objects.update(name='ali', age=23)
    print(us)
    User.objects.list()

    user3 = User(name='ali3', age=3)

    user4 = User(name='ali4', age=4)

    user5 = User(name='ali5', age=5)

    user = User.objects.filter(age=2)
    # for u in user:
    #     print(vars(u))
    # User.objects.createUser(name='ali', age=1)
    #
    # user = User.objects.get(age=1)
    # print(user)


    # print(User.objects.delete(age=2))
    # print("_------------------")
    # User.objects.list()


