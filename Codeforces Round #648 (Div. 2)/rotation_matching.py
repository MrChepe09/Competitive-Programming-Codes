def rotmatch(n, a, b):
  placea = [0]*n
  placeb = [0]*n
  diff = [0]*n
  for i in range(n):
    placea[a[i]-1] = i
  for i in range(n):
    placeb[b[i]-1] = i

  for i in range(n):
    diff[i] = (n-placea[i]+placeb[i])%n
  ats = [0]*n
  for d in diff:
    ats[d] += 1
  return max(ats)
      

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(rotmatch(n, a, b))
