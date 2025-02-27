import abc
import datetime
import time


class AbstractServer(abc.ABC):

    @abc.abstractmethod
    def receive(self):
        pass


class Server(AbstractServer):
    def receive(self):
        print("Processing your request ...")
        time.sleep(3)
        print("Done Processing ...")


class LogProxy(AbstractServer):

    def __init__(self, server):
        self.server = server

    def receive(self):
        self.logging()
        # ....
        self.server.receive()

    def logging(self):
        with open("log.log", "a") as lg:
            lg.write(f"Request {datetime.datetime.now()} \n")


def client(server, proxy):
    s = server()
    p = proxy(s)

    p.receive()

client(Server, LogProxy)