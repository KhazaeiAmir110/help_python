mabna = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
]

adad = list(input())

result = list()
sum = 0
len_ = len(adad)
for i in range(0, len(adad)):
    c = adad[len_ - i -1]
    if i == 0:
        b = (mabna.index(c) + 1) % 16
    else:
        b = (sum + mabna.index(c)) % 16
        sum = 0
        
    if b == 0:
        sum = 1
        
    result.append(mabna[b])

result = reversed(result)
print(''.join(result))    
    
    



