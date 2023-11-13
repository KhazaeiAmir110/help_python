import numpy as np

"""
عملیات های ریاضی روی آرایه ها
"""

array_1 = np.array([
    [0, 1, 2]
])
array_2 = np.array([
    [3, 4, 5]
])

print(array_1 + array_2)

print(array_1 + 1)

print(array_1 == array_2)

print(np.sum(array_1))

print(array_1.min())
print(array_1.max())
