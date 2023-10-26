from collections import Counter
a = input()
r,y,g = a.count('R'),a.count('Y'),a.count('G')
if (r>=3) or (r>=2 and y>=2) or g==0  :
      print ('nakhor lite')
else :
          print("rahat baash")
