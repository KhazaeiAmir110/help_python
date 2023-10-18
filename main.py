from multiprocessing import Process
import time


start = time.perf_counter()
def show(name):
    print(f'Starting {name} ...')
    time.sleep(2)
    print(f'Ending {name} ...')

end = time.perf_counter()
def main():
    process_1 = Process(target=show, args=('One',))
    process_2 = Process(target=show, args=('Two',))

    process_1.start()
    process_2.start()

    print('live process 1 : ' + str(process_1.is_alive()))
    print('live process 2 : ' + str(process_2.is_alive()))

    process_1.kill()
    process_2.kill()

    process_1.join()
    process_2.join()

    print('live process 1 : ' + str(process_1.is_alive()))
    print('live process 2 : ' + str(process_2.is_alive()))
    ()
    print(round(end - start))


if __name__ == '__main__':
    main()