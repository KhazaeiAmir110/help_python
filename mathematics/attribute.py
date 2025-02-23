class PersonObject:
    name = "amir"
    age = 33


p1 = PersonObject()
print(getattr(PersonObject, "name"))  # amir
print(getattr(PersonObject, "age"))  # 33

setattr(PersonObject, "family", "kh")  # set => family = kh
print(getattr(PersonObject, "family"))  # kh

print(hasattr(PersonObject, "age"))  # True


class Person:
    name = "amir"
    age = 33

    def __getattribute__(self, attr):
        if attr == "name":
            return "You cat not access name ..."
        else:
            return super().__getattribute__(attr)

    def __getattr__(self, attr):
        return f"{attr} doesn't exist ..."

    def __setattr__(self, attr, value):
        if attr == "family":
            print(f"{attr} doesn't set ...")
        else:
            return super().__setattr__(attr, value)


p2 = Person()

print(p2.agde)

p2.family = "kh"
