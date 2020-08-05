def physicist(arr):
    sumx = 0
    sumy = 0
    sumz = 0
    for i in arr:
        sumx += i[0]
        sumy += i[1]
        sumz += i[2]
    return "YES" if (sumx == 0 and sumy == 0 and sumz == 0) else "NO"


n = int(input())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
print(physicist(arr))
