def business(k, a):
    a.sort(reverse=True)
    n = 0
    res = 0
    i = 0
    while(n<k and i<len(a)):
        n+=a[i]
        res += 1
        i+=1
    if(n>=k):
        return res
    else:
        return -1
k = int(input())
a = list(map(int, input().split()))
print(business(k, a))