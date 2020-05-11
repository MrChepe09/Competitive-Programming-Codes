def triplesort(n, k, p):
  ans = []
  sorte = [False]*n
  fcount = n
  for j in range(n):
    if(p[j]==j+1):
      sorte[j] = True
      fcount-=1
        
  #Only 2 Sorted
  for j in range(n):
    if(sorte[j] != True):
      a = p[j]
      b = p[a-1]
      c = p[b-1]
      if(c!=j+1 and c!=a):
        fcount-=2
        p[j]=c
        sorte[a-1]=True
        sorte[b-1]=True
        ans.append([j+1, a, b])

  #All 3 Sorted
  for j in range(n):
    if(sorte[j] != True):
      a = p[j]
      b = p[a-1]
      c = p[b-1]
      if(c==j+1 and c!=a):
        fcount-=3
        sorte[j]=True
        sorte[a-1]=True
        sorte[b-1]=True
        ans.append([j+1, a, b])

  #Only 1 Sorted
  pairs = []
  index = []
  for j in range(n):
    if(sorte[j] != True):
      a = p[j]
      b = p[a-1]
      c = p[b-1]
      if(c==a):
        sorte[a-1]=True
        pairs.append(a)
        pairs.append(b)
        index.append(j+1)
        index.append(a)

  #print(ans, fcount, pairs)
  if(int(len(pairs)/2)%2==1):
    return -1
  else:
    for j in range(0, len(pairs), 4):
      fcount-=4
      ans.append([index[j], index[j+1], index[j+2]])
      ans.append([index[j], index[j+3], index[j+2]])
  #print(ans, fcount)
  if(len(ans)<=k):
    return ans

        
test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  p = list(map(int, input().split()))
  z = triplesort(n, k, p)

  if(z==-1):
    print(-1)
  else:
    print(len(z))
    for j in range(len(z)):
      print(*z[j])
