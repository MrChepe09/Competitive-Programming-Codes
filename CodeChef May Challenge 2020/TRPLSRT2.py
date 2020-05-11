def triplesort(n, k, p):
  ans = []
  sorte = [False]*n
  fcount = n
  #Generating Boolean Array
  for j in range(n):
    if(p[j]==j+1):
      sorte[j] = True
      fcount-=1
  c = check(fcount, ans)
  if(c!=-1 and c!=2):
    return ans
  elif(c==2):
    return -1
        
  #Sorting 2 pairs
  for j in range(n):
    if(sorte[j] != True):
      a = p[j]
      b = p[a-1]
      c = p[b-1]
      if(c==a):
        if(p[j+1] == b):
          c = p[j+2]
          d = j+2
        else:
          c = p[j+1]
          d = j+1
        ans.append([j+1, a, d+1])
        sorte[a-1]=True
        fcount-=1
        p[j]=c
        p[d]=b
  #print(p, sorte)
  c = check(fcount, ans)
  if(c!=-1 and c!=2):
    return ans
  elif(c==2):
    return -1
  
  #Sorting remaining 3 with 2 sorts
  for j in range(n):
    if(sorte[j]!=True):
      a = p[j]
      b = p[a-1]
      c = p[b-1]
      if(c!=j+1 and c!=a):
        sorte[a-1]=True
        sorte[b-1]=True
        p[j] = c
        fcount-=2
        ans.append([j+1, a, b])
  #print(p, sorte)
  c = check(fcount, ans)
  if(c!=-1 and c!=2):
    return ans
  elif(c==2):
    return -1
  

  for j in range(n):
    if(sorte[j] != True):
      a = p[j]
      b = p[a-1]
      c = p[b-1]
      if(c==j+1 and c!=a):
        sorte[j]=True
        sorte[a-1]=True
        sorte[b-1]=True
        fcount-=3
        ans.append([j+1, a, b])
  c = check(fcount, ans)
  if(c!=-1 and c!=2):
    return ans
  #print(fcount, ans, p)
  return -1
  
#Check for sorted array
def check(fcount, ans):
  #print(fcount, len(ans))
  if(fcount==0 and len(ans)<=k):        
    return ans
  elif(fcount==2):
    return 2
  else:
    #print(ans)
    return -1
  
    
test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  p = list(map(int, input().split()))
  z = triplesort(n, k, p)
  #print(z)
  if(z==-1):
    print(-1)
  else:
    print(len(z))
    for j in range(len(z)):
      print(*z[j])
