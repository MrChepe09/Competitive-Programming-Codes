def chess(n, m, a):
    c = 0
    for i in range(n):
        if(m%2==0):
            c+=1
        for j in range(m):
            c+=1
            if(a[i][j]=='.'):
                if(c%2==0):
                    a[i][j] = 'B'
                else:
                    a[i][j] = 'W'
    return a


n, m = map(int, input().split())
a = []
for i in range(n):
    mat = list(input())

    a.append(mat)
ans = chess(n, m, a)
for i in ans:   
    print(''.join(i))