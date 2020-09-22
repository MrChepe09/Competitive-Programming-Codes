def bicycle(n, a, m, b):
    maxi = -1
    for i in range(n):
        for j in range(m):
            ratio = b[j]/a[i]
            if(ratio==int(ratio)):
                maxi = max(maxi, ratio)
    count = 0
    for i in range(n):
        for j in range(m):
            if (b[j]/a[i])==maxi:
                count+=1
    return count


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
print(bicycle(n, a, m, b))