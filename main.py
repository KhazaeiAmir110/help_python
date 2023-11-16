import numpy as np

"""
Sorting, searching, and counting

"""

array_number_1 = np.array([8, 7, 6, 5, 43, 2, 23, 5, 6, 6, 4, 3, 0,0,0])

array_number_2 = np.array([
    [43, 4, 34, 3, 43],
    [100, 12, 1, 2, 33]
])

array_name = ('amir', 'reza', 'ali', 'dfd', 'amir')

# Sort
# method 1 => new array
array_new = np.sort(array_number_1)
print(array_new)
# method 2 => sort in array
array_number_2.sort()
print(array_number_2)
# method 3 => sort by index => output = index array
print(np.argsort(array_number_1))

# Searching
# max , min => output index
print(np.argmax(array_new))
print(np.argmin(array_number_1))
# Condition
a = np.extract(np.mod(array_number_1, 2)==0, array_number_1)
print(a)

# cont => شماش اعداد غیر 0
b = np.count_nonzero(array_number_1)
print(b)
