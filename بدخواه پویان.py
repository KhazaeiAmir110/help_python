p , d = map(int ,input().split())
amir = True
i = 2
s = d
while amir :
      if 0 <= s%p <= p//2 :
            print(s)
            amir = False
      else :
            s = d * i
            i += 1
