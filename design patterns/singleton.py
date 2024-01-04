class Singleton_test:
    _instance = None
    def __init__(self):
        raise ValueError("Instance")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


a = Singleton_test.get_instance()
b = Singleton_test.get_instance()

print(id(a))
print(id(b))
print(a is b) # True

# metaclass

class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(* args, ** kwargs)
        return self._instance


class Test(metaclass=Singleton):
    pass

one = Test()
two = Test()

print(one is two)


