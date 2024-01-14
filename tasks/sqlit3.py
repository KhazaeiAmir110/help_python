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
            # print(vars(_user))
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

    def __new__(cls, *args, **kwargs):
        import sqlite3
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)")
        for user in cls.objects.users:
            c.execute("INSERT INTO users VALUES (:name, :age)", user.__dict__)
            conn.commit()
        c.execute("SELECT * FROM users")
        rows = c.fetchall()
        for user in rows:
            r = dict(user)
            cls.objects.append(r)
        for user in cls.objects.users:
            print(user['name'], user['age'])

        # rows = c.fetchall()
        # print(rows[0])
        # for row in rows:
        #     r = dict(row)
        #     cls.objects.append(r)



if __name__ == '__main__':
    # user1 = User(name='ali', age=2)
    User.objects.create(name='ali', age=2)

    # user2 = User(name='ali2', age=2)
    #
    # user3 = User(name='ali3', age=3)
    #
    # user4 = User(name='ali4', age=4)
    #
    # user5 = User(name='ali5', age=5)

    # user = User.objects.filter(age=2)
    # for u in user:
    #     print(vars(u))
    # User.objects.createUser(name='ali', age=1)
    #
    # user = User.objects.get(age=1)
    # print(user)
    # User()

    print(User.objects.delete(age=2))
    print("------------------")
    User.objects.list()
    print(User.objects.users)



# --------------------------------------------------------------
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
# c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)")
# for user in self.objects.users:
#     c.execute("INSERT INTO users VALUES (:name, :age)", user.__dict__)
#     conn.commit()
c.execute("SELECT * FROM users")
rows = c.fetchall()


class Manager:
    def filter(self,*args, **kwargs):
        list_filter = list()
        for row in rows:
            for key, value in kwargs.items():
                if value in row:
                    list_filter.append(row)
        return list_filter

    def get(self, *args, **kwargs):
            get_list = list()
            for row in rows:
                for key, value in kwargs.items():
                    if value in row:
                        get_list.append(row)
            if len(get_list) == 0:
                return None
            elif len(get_list) > 1:
                return ValueError("ERROR : User More than one")
            else:
                return get_list[0]

    def delete(self, *args, **kwargs):
        geting = self.get(*args, **kwargs)
        if type(geting) is tuple:
            for key , value in kwargs.items():
                key_=key
                value_=value
            c.execute("DELETE from users where ? = ?", (key_, value_))
            conn.commit()
            return True
        else:
            raise ValueError("ERROR :Not delete")


    def list(self):
        for row in rows:
            print(row)

class Person:
    object = Manager()
    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = Person("John", 12)



# print(Person.object.filter(name = "ali"))
# print(Person.object.get(name = "ali"))
Person.object.list()
print("-----------------------")
a = Person.object.delete(name='ali4')

print(a)
