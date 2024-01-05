class Person:
    age = None
    weight = None

    @staticmethod
    def move():
        return "Milad"

    @classmethod
    def print_weight(cls):
        if cls.weight is None:
            cls.weight = 13
        return cls.weight

    def object_(obj):
        obj.weight = 1
        return obj.weight


if __name__ == '__main__':
    p1 = Person()
    Person.print_weight()  # weight_class = 13
    Person.object_(p1)  # weight_obj = 1
    print(Person.weight)
    print(p1.weight)
    print(Person.move())  # staticmethod