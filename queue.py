from multiprocessing import Process

numbers = []

def one_process_function():
    global numbers
    numbers.extend([1,2,3])
    print(f'one_process : {numbers}')

def second_process_function():
    global numbers
    numbers.extend([4,5,6])
    print(f'second_process : {numbers}')

process_1 = Process(target=one_process_function)
process_2 = Process(target=second_process_function)

process_1.start()
process_2.start()
process_1.join()
process_2.join()

# در این قسمت لیست ما تهی است زیرا هر فرآیند در یک حافضه جدا گانه هستند
print(numbers)
