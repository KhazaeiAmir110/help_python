def Paskal(n) : 
    for p in range(0, n) : 
        for i in range(0, p + 1) : 
            print(lC(p, i)," ", end = "") 
        print() 
def lC(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1)  
    return res 
n = int (input ())
Paskal(n) 
