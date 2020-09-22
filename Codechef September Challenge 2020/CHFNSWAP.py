from math import modf, sqrt, ceil
def swapchef(n):
    res = 0
    total = n*(n+1)//2
    half = (total//2)
    if(total%2==1):
        return 0
    k = sqrt(8*(half)+1)
    div = (k/2)-0.5

    part = modf(div)
    deci = part[0]
    #print(inti, deci)
    inti = int(div)
    if(deci==0):
        res = (((inti-1)*(inti))//2) + (((n-inti-1)*(n-inti))//2)

    res += n-inti
    return res

test = int(input())
for i in range(test):
    n = int(input())
    print(swapchef(n))