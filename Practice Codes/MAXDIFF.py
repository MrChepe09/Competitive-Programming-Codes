def maxdiff(n, a, k):
  c1 = 0
  c2 = 0
  asum = sum(a)
  for j in range(k):
    c1 += a[j]
  for j in range(k):
    c2 += a[n-j-1]
  return max(abs(c1-(asum-c1)), abs(c2-(asum-c2)))


test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  a.sort()
  print(maxdiff(n, a, k))
