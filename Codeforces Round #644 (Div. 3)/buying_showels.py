def shovels(n, k):
  ans = n
  for j in range(1, int(n**0.5)+1):
    if(n%j==0):
      if(j<=k):
        ans = min(ans, n//j)
      if(n//j<=k):
        ans = min(ans, j)
  return ans

test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  print(shovels(n, k))
