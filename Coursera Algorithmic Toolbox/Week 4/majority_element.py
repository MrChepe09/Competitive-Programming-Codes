def majority(n, a):
  d = {}
  half = int(n/2)
  for i in range(n):
    if(a[i] not in d):
      d[a[i]] = 1
    else:
      d[a[i]] += 1
  g = max(d, key=d.get)
  #print(g, d)
  if(d[g]>half):
    return 1
  return 0

n = int(input())
a = list(map(int, input().split()))
print(majority(n, a))
