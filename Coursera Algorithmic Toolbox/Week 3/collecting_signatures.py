def signature(m, n, a):
  count = 0
  ans = [0]*(m+1)
  
  for i in range(1, m+1):
    t = 0
    while(t<n):
      if(i>=a[t][0] and i<=a[t][1]):
        ans[i]+=1
      t+=1
  
  return ans

n = int(input())
a = []
m = 0
for i in range(n):
  p = list(map(int, input().split()))
  m = max(m, max(p))
  a.append(p)
print(signature(m, n, a))
