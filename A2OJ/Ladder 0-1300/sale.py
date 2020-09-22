def sale(n, m, a):
    a.sort()
    c = 0
    res = 0
    for i in a:
        if(c==m):
            break
        if(i<0):
            res += abs(i)
            c+=1
    return res

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(sale(n, m, a))