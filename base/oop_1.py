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

# a = Base()


# Encapsulation


