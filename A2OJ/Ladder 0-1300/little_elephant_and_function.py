def elephant(n):
    ans = []
    ans.append(n)
    for i in range(1, n):
        ans.append(i)
    return ans

n = int(input())
print(*elephant(n))