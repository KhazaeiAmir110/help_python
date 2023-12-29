
def sum_list(one,second):
    list_one = list(map(int,one))
    list_two = list(map(int,second))

    if len(list_one) != len(list_two):
        print("ERROR!!!!!!!!!")

    print(list(map(sum, zip(list_one, list_two))))

# Use of the library numpy
import numpy as np

def numpy_split(one,second):
    list_one =  np.array(one, dtype=int)
    list_two =  np.array(second, dtype=int)

    list_ = sum([list_one,list_two])
    print(list_)



# OUTPUT

list_one = list((input('Enter list one: ')).split())
list_two = list((input('Enter list tw0: ')).split())


sum_list(list_one, list_two)
print("--------------------")
numpy_split(list_one, list_two)