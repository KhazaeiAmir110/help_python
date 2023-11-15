import numpy as np

"""
Universal functions  => ufunc

vectorized : زمانی اتفاق می افتد که این کتاب خانه کد برنامه را به زبان پایتون اجرا نمیکند 
بلکه به زبان سی اجرا میکند به دلیل سرعت بیشتر برنامه

در آرایه پایتون هر نوع داده ای میتوان نوشت بلی در آرایه این کتابخانه فقط یک نوع داده در آرایه وجود دارد تا سرعت را بالا ببرد
"""

# طبق آرایه اول ، آرایه دوم را n برابر میکند
array_1 = np.multiply.outer([1,2,3,4,5], [4,5,6])
print(array_1)

# ضرب اعداد داخل آرایه و خروجی جواب فقط آرایه تک بعدی
array_2 = np.multiply.reduce([1,2,3,4,5])
print(array_2)

# مشخص کردن n * m بودن آرایه
array_3 = np.arange(8).reshape((2,4))
array_4 = np.arange(8).reshape((2,2,2))
print(array_3)
print(array_4)

# جمع عناصر داخل یک آرایه
array_5 = np.add.reduce(np.arange(-10,11))
print(array_5)
