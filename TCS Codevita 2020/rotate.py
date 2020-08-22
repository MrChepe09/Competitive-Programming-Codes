def shift(a, s, n, m):
    arr = []
    done = []
    for i in range(s, n):
        for j in range(s, m):
            if(i == s and [i, j] not in done):
                arr.append(a[i][j])
                done.append([i, j])
    for i in range(s, n):
        for j in range(s, m):
            if(i!=s and j==m-1 and [i, j] not in done):
                arr.append(a[i][j])
                done.append([i, j])
    for i in range(n-1, s-1, -1):
        for j in range(m-1, s-1, -1):
            if(i==n-1 and j!=m-1 and [i, j] not in done):
                arr.append(a[i][j])
                done.append([i, j])
    for i in range(n-1, s-1, -1):
        for j in range(m-1, s-1, -1):
            if(i!=n-1 and j==s and [i, j] not in done):
                arr.append(a[i][j])
                done.append([i, j])
    return arr
def change(arr, l, t):
    new = list(arr)
    if(t%2==1):
        for i in range(len(arr)):
            new[(i+l)%len(arr)] = arr[i]
    else:
        for i in range(len(arr)-1, -1, -1):
            new[(i-l)%len(arr)] = arr[i]
    #print(new)
    return new

def apply(a, arr, s, n, m):
    d = 0
    done = []
    for i in range(s, n):
        for j in range(s, m):
            if(i == s and [i, j] not in done):
                a[i][j] = arr[d]
                done.append([i, j])
                d+=1
    for i in range(s, n):
        for j in range(s, m):
            if(i!=s and j==m-1 and [i, j] not in done):
                a[i][j] = arr[d]
                done.append([i, j])
                d+=1
    for i in range(n-1, s-1, -1):
        for j in range(m-1, s-1, -1):
            if(i==n-1 and j!=m-1 and [i, j] not in done):
                a[i][j] = arr[d]
                d+=1
                done.append([i, j])
    for i in range(n-1, s-1, -1):
        for j in range(m-1, s-1, -1):
            if(i!=n-1 and j==s and [i, j] not in done):
                a[i][j] = arr[d]
                d+=1
                done.append([i, j])
    return a
    
def rotate(n, m, a, l):
    start = 0
    for i in range(len(l)):
        arr = shift(a, start, n, m)
        #print(arr)
        ch = change(arr, l[start], start)
        res = apply(a, ch, start, n, m)
        n-=1
        m-=1
        start += 1
    return res

n, m = map(int, input().split())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
layer = list(map(int, input().split()))
ans = rotate(n, m, arr, layer)
for i in range(len(ans)):
    print(*ans[i])
