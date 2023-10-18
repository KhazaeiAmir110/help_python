from multiprocessing import Process
import time
import sys

start = time.perf_counter()
def show(name):
    print(f'Starting {name} ...')
    time.sleep(2)
    print(f'Ending {name} ...')

end = time.perf_counter()
def main():
    p1 = Process(target=show, args=('One',), daemon=True)
    p2 = Process(target=show, args=('Two',))

    p1.start()
    p2.start()
    print(round(end - start))
    sys.exit()

if __name__ == '__main__':
    main()