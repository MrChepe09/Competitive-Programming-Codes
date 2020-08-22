def cupboard(n, l, r):
    lcount = l.count(1)
    rcount = r.count(1)
    li = min(lcount, n-lcount)
    ri = min(rcount, n-rcount)

    return li+ri
    
n = int(input())
larr = []
rarr = []
for i in range(n):
    l, r = map(int, input().split())
    larr.append(l)
    rarr.append(r)
print(cupboard(n, larr, rarr))