def insomania(k, l, m, n, d):
    count = 0
    arr = [0 for _ in range(d)]
    for i in range(k-1, d, k):
        arr[i] = 1
    for i in range(l-1, d, l):
        arr[i] = 1
    for i in range(m-1, d, m):
        arr[i] = 1
    for i in range(n-1, d, n):
        arr[i] = 1
    for i in range(d):
        if(arr[i]==1):
            count+=1
    return count


k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
print(insomania(k, l, m, n, d))