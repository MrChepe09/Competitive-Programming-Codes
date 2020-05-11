def signature(n, a):
  a = sorted(a, key=lambda x: x[1])
  ans = []
  start = 0
  while(start<n):
    c = a[start]
    while(start<n-1 and c[1]>=a[start+1][0]):
      start+=1
    ans.append(c[1])
    start += 1
  return ans

n = int(input())
a = []
for i in range(n):
  p = list(map(int, input().split()))
  a.append(p)
z = signature(n, a)
print(len(z))
print(*z)
