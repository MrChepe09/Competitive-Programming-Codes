def drchef(n, x, a):
    days = 0
    for i in range(n):
        #print(a)
        #For elements greater
        if(x>=a[i]):
            days+=1
            g = 2*a[i]
            if(g>x):
                x = g
            continue
        #---------------------
        #For elements smaller
        t = a[i]
        while(t>0):
            #print(1)
            days+=1
            h = 2*(t-x)
            if(h<t):
                t = h
            #print(t)
            x = 2*x
        x = 2*a[i]
        #--------------------------
    return days

test = int(input())
for i in range(test):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(drchef(n, x, a))
