from multiprocessing import Process
import time

start = time.perf_counter()
def show(name, delay):
    print(f'Starting {name} ...')
    time.sleep(delay)
    print(f'Ending {name} ...')

class ProcessClass(Process):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay
    def run(self):
        show(self.name, self.delay)

end = time.perf_counter()
def main():
    p1 = ProcessClass('name', 1)
    p2= ProcessClass('amir', 2)

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(end - start)


if __name__ == '__main__':
    main()