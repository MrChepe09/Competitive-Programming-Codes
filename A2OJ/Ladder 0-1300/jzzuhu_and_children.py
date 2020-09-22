import math
def jzzuhu(n, m, a):
    for i in range(len(a)):
        if(a[i]>0):
            a[i] = math.ceil(a[i]/m)
    #print(a)
    maxi = -1
    ans = 0
    for i in range(n):
        if(a[i]>=maxi):
            maxi = max(maxi, a[i])
            ans = i+1
    return ans
     
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(jzzuhu(n, m, a))