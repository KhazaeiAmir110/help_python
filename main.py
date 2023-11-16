import numpy as np

"""
Structured arrays
در بعضی مواقع نیاز است که ما در آرایه خود ، بیش از یک نوع داده را استفاده کنیم ، str , int , float , ... 
"""

array_human = np.array(
    [('amir', 20, 30.9, 'qom'), ('reza', 40, 80.9, 'tehran'), ('ali', 25, 50.9, 'mashhad')],
    dtype = [('name','<U10'), ('age','<i4'), ('weight', '<f4'), ('city', '<U10')]
)
print(array_human)

print(array_human[0]['name'])

for record in array_human:
    if record['age'] >= 25 :
        print(record)