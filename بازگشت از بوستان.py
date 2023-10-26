a,b = input().split()
c,d = input().split()
a=int(a)
b=int(b)
c=int (c)
d=int(d)
if a>c and b>d :
      print ('Left')
elif a>c and b<d :
     print ('Left')
elif a<c and b>d :
     print ('Right')
elif a<c and d>b :
     print ('Right')
elif a>c and b==d :
      print ('Left')
elif a<c and b==d :
       print ('Right')
