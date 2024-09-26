import abc


class Validation:

    def validate_password(self, password: str):
        pass

    def validate_username(self, username: str):
        pass


class User(metaclass=abc.ABC, Validation):
    birth_date = None
    mobile = None
    generate = None

    __username = None
    __password = None

    def set_password(self, password: str):
        self.__validation.validate_password(password)

    def set_username(self, username: str):
        self.__validation.validate_username(username)


class Employee(User):
    pass


if __name__ == '__main__':
    employee = Employee()
    password = "13e3q43"

    employee.set_password(password)
