def triplesort(n, k, p):
  ans = []
  sorte = [False]*n
  for j in range(n):
    if(p[j]==j+1):
      sorte[j] = True
  s = 0
  while(s!=n):
    if(sorte.count(False)==2 or len(ans)>k):
      return -1
    if(sorte.count(False)==0):
      return ans
    while(sorte[s]==True):
      s+=1
    a = p[s]
    b = p[a-1]
    c = p[b-1]
    if(c==s+1 and c!=a):
      sorte[s]=True
      sorte[a-1]=True
      sorte[b-1]=True
      ans.append([s+1, a, b])
    elif(c!=s+1 and c!=a):
      sorte[a-1]=True
      sorte[b-1]=True
      p[s] = c
      ans.append([s+1, a, b])
    elif(c==a):
      for x in range(s+1, len(p)):
        if(p[x]!=b and sorte[x]==False):
          c = p[x]
          break
      #print(a, b, c)
      ans.append([s+1, a, x+1])
      sorte[a-1]=True
      p[s]=c
      p[x]=b   
      
      
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
