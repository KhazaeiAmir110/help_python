class Teacher:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name, teacher):
        self.name = name
        self._teacher = Teacher(teacher)
