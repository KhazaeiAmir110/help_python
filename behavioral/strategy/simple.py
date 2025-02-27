import abc


class Read:

    def __init__(self, sentence):
        self.sentence = sentence
        self._direction = None

    def set_direction(self, direction):
        self._direction = direction

    def read(self):
        return self._direction.direct(self.sentence)


class DirectionStrategy(abc.ABC):

    @abc.abstractmethod
    def direct(self, data):
        pass


class Right(DirectionStrategy):
    def direct(self, data):
        print(data[::-1])


class Left(DirectionStrategy):
    def direct(self, data):
        print(data[::1])


c = Read('hellow word')
c.set_direction(Right())
c.read()
