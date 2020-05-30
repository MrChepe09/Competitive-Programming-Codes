def honestcoach(n, a):
  mini = 100000
  a.sort()
  for i in range(n-1):
    sub = a[i+1]-a[i]
    mini = min(mini, sub)
  return mini

test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(honestcoach(n, a))
