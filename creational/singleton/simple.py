class Person:
    _instance = None

    def __init__(self, *args, **kwargs):
        raise RuntimeError("call get_instance")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


object_1 = Person.get_instance()
object_2 = Person.get_instance()
print(object_1 is object_2)


# singleton by metaclass

class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super.__call__()
        return self._instance


class One(metaclass=Singleton):
    pass


one_1 = One()
one_2 = One()

print(one_1 is one_2)
