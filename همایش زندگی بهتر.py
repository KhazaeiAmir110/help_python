r, c = map(int, input().split())
if c<=10 :
     s='Right'
else :
     s = 'Left'
if s == 'Right' :
     w = c
else :
     w =  (20 - c) + 1
row = (10 - r) + 1
print(s, row, w)
