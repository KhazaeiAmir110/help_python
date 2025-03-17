class A:
    # def __new__(cls, *args, **kwargs):
    #     print(cls)
    pass


ob = A()
print(ob.__class__)

# class by type
person = type("Person", (), {"name": "amir"})
print(person)


class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class db(metaclass=Singleton):
    pass
