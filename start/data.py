class Person:
    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.family = kwargs['family']
        self.age = kwargs['age']
        self.email = kwargs['email']
        self.phone = kwargs['phone']
        self.address = kwargs['address']
        self.birthday = kwargs['birthday']
        self.gender = kwargs['gender']

person_1 = Person(name="amir", family='df', age=20, email="<EMAIL>", phone="02442424242", address="sdfsdfsddff", birthday="dfd", gender="female")
person_2 = Person(name="alice", family='df', age=20, email="<EMAIL>", phone="02442424242", address="sdfsdfsdf", birthday="sdfd", gender="female")

content = {
    'person_1': person_1,
    'person_2': person_2,
    'name': 'Amir',
    'age': 20,
    'list': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'dict': [
        {'name': 'John', 'age': -12},
        {'name': 'Aer', 'age': 23},
        {'name': 'Jan', 'age': 19},
        {'name': 'are', 'age': 40},
        {'name': 'John', 'age': 42},
    ]
}