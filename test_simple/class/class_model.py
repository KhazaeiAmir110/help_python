class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def full_name(self):
        return self.name + " " + self.family

    def email(self):
        return f"{self.full_name()}@gmail.com".replace(' ', '')
