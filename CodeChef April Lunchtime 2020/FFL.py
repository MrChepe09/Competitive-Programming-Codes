def league(n, a, b):
  sumc = 0
  min1 = 101
  min0 = 101
  for j in range(n):
    if(b[j]==1):
      min1 = min(min1, a[j])
    else:
      min0 = min(min0, a[j])
  return min1+min0

test = int(input())
for i in range(test):
  n, cost = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  ans = league(n, a, b)
  if(ans+cost>100):
    print("no")
  else:
    print("yes")
