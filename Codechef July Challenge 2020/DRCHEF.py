import math
def check(n, x, a):
    #print(x, a)
    if(x>=a[0]):
        return n
    else:
        k = a[-1]/x
        lg = math.ceil(math.log(k, 2.0))
        return (lg+n)
    
def drchef(n, x, a):
    days = 0
    b = list(a)
    while(True):
        ele = 1000000001
        for i in range(n):
            if(a[i]>=x and a[i]<ele):
                ele = a[i]
                g = i
        
        if(ele==1000000001):
            break
        #print(a[g], x)
        a[g] -= x
        a[g] *= 2
        if(a[g]>b[g]):
            a[g]=b[g]
        x *= 2
        days += 1
        print(a)
    zero = 0
    
    for i in range(n):
        if(a[i] > 0):
            zero += 1
    return days+zero
            
            

test = int(input())
for i in range(test):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(check(n, x, a))
    print(drchef(n, x, a))
    
