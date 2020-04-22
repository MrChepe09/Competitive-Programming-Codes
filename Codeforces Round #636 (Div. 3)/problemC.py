def problemC(n, a):
  maxs = a[0]
  if(a[0]>=0):
    ls = 1
    for j in range(0, len(a)):
      if(a[j]<0):
        break
      else:
        maxs = max(maxs, a[j])
  else:
    ls = 0
    for j in range(0, len(a)):
      if(a[j]>0):
        break
      else:
        maxs = max(maxs, a[j])
  t = a.index(maxs)
  #print(t, maxs)
  #1=p, 0=n
  minn = -1000000001
  maxp = 0
  for j in range(t+1, len(a)):
    if(ls==1):
      if(a[j]<0):
        minn = max(minn, a[j])
        if(j==(n-1)):
          maxs+=minn
      else:
        if(minn!=-1000000001):
          maxs += minn
          ls = 0
        maxp = a[j]
        if(j==len(a)-1 and ls ==0):
          maxs+=maxp
    else:
      if(a[j]>0):
        maxp = max(maxp, a[j])
        if(j==(n-1)):
          maxs+=maxp
      else:
        if(maxp!=0):
          maxs += maxp
          ls = 1
        minn = a[j]
        if(j==len(a)-1 and ls==1):
          maxs+=minn
  return maxs

test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(problemC(n, a))
