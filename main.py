class Person:
    __name = None
    age = None

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_person(self):
        property(get_person)

person = Person()
person.set_name("amir")
pe = Person()
print(pe.name)

print(person.get_name())