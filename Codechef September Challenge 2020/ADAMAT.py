def adamat(n, a):
    ca = 0
    cb = 0
    i=1
    while(i<n):
        if a[i][0] != i+1:
            i+=1
            break
        else:
            ca = 1
        i+=1
    while(i<n):
        if a[0][i] != i+1 and a[0][i-1] == i:
            cb+=2
        i+=1
    #print(ca, cb)
    return ca+cb

test = int(input())
for _ in range(test):
    mat = []
    n = int(input())
    for i in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    print(adamat(n, mat))
