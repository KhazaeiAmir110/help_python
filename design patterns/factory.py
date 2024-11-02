# Factory Method
"""
    Factory => 3 component : 1. creator, 2. product, 3. clint
"""
from abc import ABC, abstractmethod


# Example 1
class File(ABC):
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        return self.make().edit(self.file)


class Json:
    def edit(self, file):
        return f"Working show this {file} JSON..."


class Xml:
    def edit(self, file):
        return f"Working show this {file} XML..."


class YAML:
    def edit(self, file):
        return f"Working show this {file} YAML..."


class JsonFile(File):
    def make(self):
        return Json()


class XmlFile(File):
    def make(self):
        return Xml()


class YAMLFile(File):
    def make(self):
        return YAML()


def client_file(file, format):
    formats = {
        "json": JsonFile,
        "xml": XmlFile,
        "yaml": YAMLFile,
    }
    result = formats[format](file)
    return result.call_edit()


# Example 2
# type tire => generic
class Bicycle1:
    def __init__(self):
        self.tire = GenericTires()

    def get_tire_type(self):
        return self.tire.tire_type()


class GenericTires:
    def tire_type(self):
        return "generic"


# bike = Bicycle1()
# print(bike.get_tire_type())

# add type tire mountain
class MountainTires:
    def tire_type(self):
        return "mountain"


class Bicycle2:
    def __init__(self, tire_type: str):
        self.tire_type = tire_type
        self.tires = self.add_tires()

    def add_tires(self):
        if self.tire_type == "generic":
            return GenericTires()
        elif self.tire_type == "mountain":
            return MountainTires()

    def get_tire_type(self):
        return self.tires.tire_type()


# bike = Bicycle2("mountain")
# print(bike.get_tire_type())


# factory
class Bicycle:
    def __init__(self, factory):
        self.tires = factory().add_tires()


class GenericFactory:
    def add_tires(self):
        return GenericTires()


class MountainFactory:
    def add_tires(self):
        return MountainTires()

# bike = Bicycle(GenericFactory)
# print(bike.tires.tire_type())
