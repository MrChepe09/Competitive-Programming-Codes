def equations(n, m):
    count = 0
    for i in range(0, 1001):
        for j in range(0, 1001):
            if (i**2)+j==n and (j**2)+i==m:
                count+=1
    return count


n, m = map(int, input().split())
print(equations(n, m))