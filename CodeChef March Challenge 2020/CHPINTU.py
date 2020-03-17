test = int(input())
for i in range(test):
  fdone = []
  pdone = []
  m, n = map(int, input().split())
  f = list(map(int, input().split()))
  p = list(map(int, input().split()))
  for j in range(m):
    if(f[j] not in fdone):
      fdone.append(f[j])
      pdone.append(p[j])
    else:
      pdone[fdone.index(f[j])] += p[j]
  print(min(pdone))
  
