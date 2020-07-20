def doofcart(n, a, p):
    count = 0
    sumg = p[0]+p[1]
    ind = binarysearch(a, sumg)
    if(ind>=0 and a[ind]==sumg):
        return -1
    else:
        return ind+1

def binarysearch(ar, key):
    l, r = 0, len(ar) - 1
    while 1:
        mid = l + r >> 1
        if l == mid:
            if ar[r] <= key: return r
            elif ar[l] <= key: return l
            else: return l - 1
        elif ar[mid] <= key:
            l = mid
        else:
            r = mid

test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        p = list(map(int, input().split()))
        print(doofcart(n, a, p))
