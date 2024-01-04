"""
    Facade
    - a structural design pattern that provides a simplified interface to a library,
    a framework, or any other complex set of classes.
"""

class CPU:
    def extract(self):
        print("Extract")

class Memory:
    def load(self):
        print("Loading data ...")

class SSD:
    def read(self):
        print("Read data ...")

# Facade
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SSD()

    def start(self):
        self.memory.load()
        self.ssd.read()
        self.cpu.extract()


def client():
    facade = Computer()
    facade.start()

client()