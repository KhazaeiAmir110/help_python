a , b =  (input().split())
a = int(a)
b = int(b)
r = 1
j = []
o=0
while o != 1000 :
     for i in range (1 , a+1) :
          j.append(i)
     o+=1         
t = j[0::b]
del t[0]
e = []
for i in t :
     e.append(i)
     if i == 1 :
          break
print (len(e))
