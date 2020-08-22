def chocolates(x, y):
    if(y==1):
        return x
    if(x==y):
        return 1
    else:
        return 1 + chocolates(max(x-y, y), min(x-y, y))
    
minl = int(input())
maxl = int(input())
minw = int(input())
maxw = int(input())
res = 0
for i in range(minl, maxl+1):
    for j in range(minw, maxw+1):
        res+=chocolates(max(i, j), min(i, j))
print(res)
    
