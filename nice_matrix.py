def matrix(n, m, a):
    res = 0
    for i in range(n):
        for j in range(m):
            x = abs(a[n-i-1][j]-a[i][j]) + abs(a[i][m-j-1]-a[i][j])
            y = abs(a[i][j]-a[n-i-1][j]) + abs(a[i][m-j-1]-a[n-i-1][j])
            z = abs(a[n-i-1][j]-a[i][m-j-1]) + abs(a[i][j]-a[i][m-j-1])
            if x<=y and x<=z:
                res += x
                a[n-i-1][j]=a[i][j]
                a[i][m-j-1]=a[i][j]
            elif y<=x and y<=z:
                res += y
                a[i][j]=a[n-i-1][j]
                a[i][m-j-1]=a[n-i-1][j]
            elif(z<=x and z<=y):
                res += z
                a[n-i-1][j]=a[i][m-j-1]
                a[i][j]=a[i][m-j-1]
    return res
        
test = int(input())
for i in range(test):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        g = list(map(int, input().split()))
        a.append(g)
    print(matrix(n, m, a))
