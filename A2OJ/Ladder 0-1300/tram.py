def tram(n, a):
    train = 0
    maxi = 0
    for i in range(n):
        train -= a[i][0]
        train += a[i][1]
        maxi = max(maxi, train)
    return maxi


n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
print(tram(n, arr))