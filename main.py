import numpy as np

"""
کار با متد های بیشتر numpy
عملیات هایی که میتوانیم روی آرایه ها انجام دهیم
part 2
"""

array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [100, 200, 300]
])

print(array)

# size array
print('siz = ' + str(array.size))

print('n . m = ' + str(array.shape))
# عوض کردن ساختار آرایه
print('-----------------')
print(array.reshape(5, 3))
print(array.reshape(1, 15))
print(array.reshape(15, 1))

# item [n]
print('itme[0] = ' + str(array[0]))
# one
print('itme[0][0] = ' + str(array[0][0]))
# two
print('itme[0, 0] = ' + str(array[0, 0]))
# range
print('itme[0:3] = ' + str(array[0:3]))
