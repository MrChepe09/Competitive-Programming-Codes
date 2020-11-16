def unsquers(a, mat):
    t = 0
    c = 1
    for i in range(1, n+1):
        c = 1
        t = a[i-1]
        for j in range(i, n+1):
            if a[j-1]>t:
                c+=1
                t = a[j-1]
            mat[i][j] = c
    return mat

def getmax(n, mat, res):
    maxi = -1
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            maxi = max(maxi, mat[j][i])
            res[j][i] = maxi
        maxi = -1

    return res
    
n, q, s = map(int, input().split())
last = 0
mat = [[0 for _ in range(n+1)] for _ in range(n+1)]
ares = [[0 for _ in range(n+1)] for _ in range(n+1)]
a = list(map(int, input().split()))
mat = unsquers(a, mat)
ares = getmax(n, mat, ares)
#print(mat)
for i in range(q):
    res = 0
    x, y = map(int, input().split())
    x = ((x+(s*last)-1)%n)+1
    y = ((y+(s*last)-1)%n)+1
    if x>y:
        x, y = y, x
    last = ares[x][y]
    #print(x, y)
    print(last)
