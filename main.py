from multiprocessing import Process
import time
from concurrent.futures import ProcessPoolExecutor


start = time.perf_counter()
def show(name):
    print(f'Starting {name} ...')
    time.sleep(2)
    print(f'Ending {name} ...')

end = time.perf_counter()
def main():
    with ProcessPoolExecutor(max_workers=2) as executor:
        names = ['One', 'Two', 'Three', 'Four']
        executor.map(show, names)
    print(round(end - start))


if __name__ == '__main__':
    main()