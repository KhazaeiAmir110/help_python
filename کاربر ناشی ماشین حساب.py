
n = int(input())
list_ = list()
accepted = True
for i in range(0, n):
    input_ = int(input())
    list_.append(input_)
    if input_ not in (2, 5):
        accepted = False
        
if accepted:
    a = 5
    b = 0
    c = 0
    for item in list_:
        
        b += 1
        if item == 2:
            c -= 1
            
    print(f'{a} {b} {c}')
    

    

