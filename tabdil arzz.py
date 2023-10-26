n = int(input())
x,y,z = map(int, input().split())
a,b,c = map(int, input().split())

counter = 0
if n < ( a and b and c):
    print(0)
elif n > ( x*a + y*b + z*c ):
    print(0)
elif n == ( x*a + y*b + z*c ):
    print(1)

elif (n == a and n == b) or(n == a and n == c) or (n == b and n == c) :
    if (n == a and n == b) :
            for k in range(0, z+1):
                if   k * c == n:
                    counter += 1
    elif (n == a and n == c) :
            for j in range(0, y+1):
                if  j * b == n:
                    counter += 1
    elif (n == b and n == c) :
             for i in range(0, x+1):
                if i * a   == n:
                    counter += 1
    print(counter+2)

else :
      a_2 = n // a
      b_2 = n // b
      c_2 = n // c
      if (x + y + z) < 1000 :
                for i in range(0, x+1):
                   for j in range(0, y+1):
                        for k in range(0, z+1):
                            if i * a + j * b + k * c == n:
                                counter += 1
                print(counter)
      else :
          for i in range ( 0 , a_2 + 1 ) :
                    for k in range ( 0 , c_2 + 1  ) :
                          for j in range ( 0 , b_2 + 1 ):
                               if i * a + j * b + k * c == n:
                                        counter += 1

          print(counter)
      '''else :
          if (x + y + z) < 1000 :
                for i in range(0, x+1):
                   for j in range(0, y+1):
                        for k in range(0, z+1):
                            if i * a + j * b + k * c == n:
                                counter += 1
                print(counter)
          elif 1000 < ( x + y + z ) < 2000 :
              for i in range(1000, x+1):
                   for j in range(1000, y+1):
                        for k in range(1000, z+1):
                            if i * a + j * b + k * c == n:
                                counter += 1
              print(counter)
          elif 2000 < ( x+y+z)  :
              for i in range(2000, x+1):
                   for j in range(2000, y+1):
                        for k in range(2000, z+1):
                            if i * a + j * b + k * c == n:
                                counter += 1
              print(counter)'''











 
    

