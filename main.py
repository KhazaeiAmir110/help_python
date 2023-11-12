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

array_2 = np.array([[0, 0, 0]])
array_3 = np.array([1, 1, 1, 1, 1])
# چسباندن آرایه ها به هم
# به پایین آرایه اضافه میکند
print(np.vstack((array, array_2)))
print('----------------------')
# به سمت راست آرایه اضافه میکند
print(np.hstack((array, array_3.reshape(5, 1))))

# method vstack and hstack
print(np.concatenate((array, array_2), axis=0))

# جداسازی array
print(np.vsplit(array, 5))
print(np.hsplit(array, 3))
