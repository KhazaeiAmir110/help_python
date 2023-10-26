days = ['shanbe' , '1shanbe' , '2shanbe' , '3shanbe' , '4shanbe' , '5shanbe' , 'jome']
for i in range (3) :
      add = input()
      for j in add :
            day = input().split()
            for k in day :
                  if k in days :
                        days.remove(k)
print(len(days))
'''
list_ = []
for i in range(3) :
      a = int(input())
      for i in a :
            da = input().split()
            list_.append(i)
      for j in days :
            if j in list_ :
                  days.remove(k)
print(len(days))
'''
