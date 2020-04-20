def redone(n):
  return (ans[n]-1)


ans = []
t = 1
for k in range(1, 1000001):
  t = ((t)%1000000007*k)%1000000007
  ans.append(t)
test = int(input())
for i in range(test):
  n = int(input())
  print(redone(n))
