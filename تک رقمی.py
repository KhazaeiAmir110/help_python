a= int (input ())
m = 0

while a!=0 :
        r = a % 10
        m = m + r
        a = a//10
        
        if m > 10 :
            o = 0
            while m!=0 :
                e = m %10
                o = o + e
                m = m//10
                
                if o > 10 :
                                q=0
                                while o!=0 :
                                        w = o % 10
                                        q = q + w
                                        o = o//10
                                        if q > 10 :
                                                u=0
                                                while q!=0 :
                                                        v = q%10
                                                        u = u + v
                                                        q = q//10
                                                        print (u)
                                                
                                        
if 0 < m <10 :
        print (m)
elif 0 < o < 10 :
        print (o)
elif 0<q< 10 :
        print (q)
       
        
