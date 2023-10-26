import math
a , b  =input().split()
a = int(a)
b=int(b)
def hcfnaive(a,b): 
         if(b==0): 
               return a 
         else: 
               return hcfnaive(b,a%b) 
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
num1 = a
num2 = b

print(hcfnaive(a,b), compute_lcm(num1, num2))
