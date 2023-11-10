import numpy as np

array = np.array([
    [1,2],
    [3,4],
    [5,6]
])
# type array
print(type(array))
#print
print(array)
# بعد
print(array.ndim)
# ستون و ردیف
print(array.shape)

# تبدیل نوع داده به float
# باید یک نوع داه باشد تمام داده های ما
array_2 = np.array([
    [2, 3.4]
], dtype=np.uint8)
print(array_2)
#uint8
print(array_2.dtype)