def decorator(*args, **kwargs):
    def inner(func):
        if (kwargs['role'] == "admin" and kwargs["password"] == 123):
            func()
        elif(kwargs["role"] == "admin" and kwargs["password"] != 123):
            raise ValueError("Error : password is not found ...")
        elif (kwargs["role"] == "inner"):
            def test():
                return "you are inner ..."
            return test()
        else:
            raise ValueError("Error : you are not admin!!!")
    return inner


@decorator(role="admin", password=123)
def request():
    print("This is a request ...")


request()