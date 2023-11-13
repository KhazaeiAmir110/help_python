import numpy as np

"""
Input and output
"""

array_test = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])

# save
np.save('output.npy', array_test)
np.savetxt('output.txt', array_test)

# load
print(np.load('output.npy'))

# ---------------------------------
array_new = np.arange(10, 2000)

np.savez('output.npz', array_new, array_test)

load = np.load('output.npz')
print(load)

print(load['arr_0'])
print(load['arr_1'])
