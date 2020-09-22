# 0 1 1 2 3 5 8 13 21 34

def theorem(n):
    if(n==3):
        return str(1)+" "+str(1)+" "+str(1)
    elif(n==2):
        return str(1)+" "+str(1)+" "+str(0)
    elif(n==1):
        return str(1)+" "+str(0)+" "+str(0)
    elif(n==0):
        return str(0)+" "+str(0)+" "+str(0)
    a = 5
    b = 8

    pp4 = 1
    pp3 = 1
    pp2 = 2
    pp1 = 3
    while(a!=n):
        c = a
        a = b
        b = c + b
        pp4 = pp3
        pp3 = pp2
        pp2 = pp1
        pp1 = c
        #print(b, a, pp1, pp2, pp3, pp4)
    
        
    return str(pp4)+" "+str(pp3)+" "+str(pp1)


n = int(input())
print(theorem(n))