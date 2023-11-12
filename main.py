import numpy as np

"""
کار با متد های بیشتر numpy
عملیات هایی که میتوانیم روی آرایه ها انجام دهیم
part 2
"""

array = np.array([
    [10, 2, 3],
    [42, 5, 6],
    [73, 8, 9],
    [102, 11, 12],
    [1003, 200, 300]
])

# sort array
print(np.sort(array))

# copy and view
array_2 = array.copy()  # new array
array_3 = array.view()  # array => change name

# تشخیص copy , view
print(array_2.base)  # None
print(array_3.base)  # a
