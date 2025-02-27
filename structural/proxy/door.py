from secrets import compare_digest


class Door:
    def open(self):
        pass

    def close(self):
        pass


class LabDoor(Door):
    def open(self):
        print("Opening lab door")

    def close(self):
        print("Closing the lab door")


class SecuredDoor:
    _door = None

    def __init__(self, door_request):
        self.door = door_request

    @staticmethod
    def authenticate(self, password):
        return compare_digest(password, '$ecr@t')

    def open(self, password):
        if self.authenticate(self, password):
            self.door.open()
        else:
            print("Big no! It ain't possible.")

    def close(self):
        self.door.close()


door = SecuredDoor(LabDoor())
door.open('invalid')  # Big no! It ain't possible

door.open('$ecr@t')  # Opening lab door
door.close()  # Closing Lab Door
