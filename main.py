import numpy as np

"""
random
"""
random = np.random.default_rng()
# int
test_1 = random.integers(1,10,3)
print(test_1)

# float
test_2 = random.random(3)
print(test_2)

# array
array = np.array([2,3,4,5,6,7,8])
test_3 = random.choice(array,2,p=[0.3,0,0,0.4,0,0,0.3])
print(test_3)