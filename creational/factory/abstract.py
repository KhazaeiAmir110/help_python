from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def show(self):
        pass


class B(A):
    def show(self):
        print("B show ...")


b = B()
