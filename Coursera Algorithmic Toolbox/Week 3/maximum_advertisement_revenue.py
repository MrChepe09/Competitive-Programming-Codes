def maxad(n, a, b):
  ans = 0
  for i in range(n):
    ans += (a[i]*b[i])
  return ans

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
print(maxad(n, a, b))
