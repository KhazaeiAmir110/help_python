import numpy as np

"""
متد های دیگر numpy به غیر از array
"""

# empty
array = np.empty((3, 4), dtype=np.uint8)
print(array)

# empty_like
test_array = ([1, 2, 3], [4, 5, 6])
array_1 = np.empty_like(test_array, shape=(3, 4), dtype=np.uint8)
print(array_1)

# eye => matrix I : n * m
array_2 = np.eye(4, 5)
array_3 = np.eye(4, 5, 1)
print(array_2)
print(array_3)

# identity => matrix I : n * n
array_4 = np.identity(5)
print(array_4)

# ones => matrix 1
array_5 = np.ones((2, 3))
print(array_5)

# zeros => matrix 0
array_6 = np.zeros((2, 3))
print(array_6)

# full => matrix n
array_n = np.full((3, 3), 10)
print(array_n)

# arange => m => n
array_arang = np.arange(10, 200)
print(array_arang)