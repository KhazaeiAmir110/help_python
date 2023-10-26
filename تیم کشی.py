a1 = int(input())
b1 = int (input())
a2 = int(input())
b2 = int (input())
a3 = int (input())
b3 = int (input())
r = 0
if a1==b1 :
     r+=a1
elif a1>b1:
     r+=b1
elif a1<b1 :
     r+=a1
r1 = 0
if a2==b2 :
     r1+=a2
elif a2>b2:
     r1+=b2
elif a2<b2 :
     r1+=a2
r3 = 0
if a3==b3 :
     r3+=a3
elif a3>b3:
     r3+=b3
elif a3<b3 :
     r3+=a3
print (r + r1 +r3)
