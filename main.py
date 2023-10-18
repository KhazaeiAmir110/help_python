from multiprocessing import Process
import time

start = time.perf_counter()
def show(name):
    print(f'Starting {name} ...')
    time.sleep(4)
    print(f'Ending {name} ...')

p1 = Process(target=show, args=('One',))
p2 = Process(target=show, args=('Two',))

end = time.perf_counter()



if __name__ == '__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(end - start)