import numpy as np

"""
Masked arrays => filtering datas
"""

array_1 = np.array([
    [1, 2, 3],
    [np.nan, 5, 6]
])
# فیلتر اعداد منفی
mask_array_1 = np.ma.masked_invalid(array_1)
print(mask_array_1)


array_2 = np.arange(-10, 10)
mask_array_2 = np.ma.masked_where(array_2 < 0 , array_2)
print(mask_array_2)

