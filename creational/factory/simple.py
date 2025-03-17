from abc import ABC, abstractmethod


class File(ABC):

    def __init__(self, file):
        self.file = file

    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        product = self.make()
        return product.edit(self.file)


class JsonFile(File):
    def make(self):
        return Json()


class XmlFile(File):
    def make(self):
        return Xml()


class Json:
    def edit(self, file):
        return f"working on {file} Json ..."


class Xml:
    def edit(self, file):
        return f"working on {file} Xml ..."


def client(file, format):
    formats = {
        'json': JsonFile,
        'xml': XmlFile
    }
    result = formats[format](file)
    return result.call_edit()


print(client('show', 'json'))
