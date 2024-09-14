from abc import ABC, abstractmethod


class Base(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def transfer(self):
        pass


class Concrete(Base):
    def connect(self):
        print('connect')

    def transfer(self):
        print('transfer')


# Encapsulation

class Student:
    def __init__(self):
        self.__age = 0

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @age.deleter
    def age(self):
        del self.__age


student = Student()

student.age = 22
print("age student : " + str(student.age))
del student.age
