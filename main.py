import numpy as np

"""
linspace => فاصله های دقیقا یکسان
create matrix by array
"""
array = np.linspace(1,200,num=30, retstep=True)
print(array)

# ------------------------------------
array_1 = [1,2,3,4]
array_2 = [5,6,7,8]
array_3 = [9,10,11,12]
array_4 = [13,14,15,16]

array_new = np.meshgrid(array_1,array_2,array_3,array_4)
# تمام ترکیبات بین 4 آرایه
print(array_new)
