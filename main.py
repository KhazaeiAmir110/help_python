from multiprocessing import Process , current_process
import time
import os

start = time.perf_counter()
def show(name):
    print(f'Starting {name} ...')
    time.sleep(1)
    print(current_process())
    print(f'Ending {name} ...')

def show_2(name):
    print('first : ' + name)
    print('id : ' + str(os.getpid()))
    print('parent id : ' + str(os.getppid()))

p1 = Process(target=show,name='process_1', args=('One',))
p2 = Process(target=show,name='process_2', args=('Two',))

p3 = Process(target=show_2,name='process_3', args=('One',))

end = time.perf_counter()



if __name__ == '__main__':
    p1.start()
    p2.start()
    print('live p1 : ' + str(p1.is_alive()))
    p1.join()
    p2.join()
    print(end - start)
    print('--------------------------')
    p3.start()