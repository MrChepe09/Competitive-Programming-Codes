test = int(input())
for i in range(test):
  n, q = map(int, input().split())
  nlist = list(map(int, input().split()))
  for j in range(q):
    x1, x2, y = map(int, input().split())
    ans = 0
    for k in range(x1, x2-1):
      if(y>nlist[k] and (nlist[k+1]>=y)):
        ans += 1
      elif(y<nlist[k] and (nlist[k+1]<=y)):
        ans += 1
      elif(y==nlist[j]):
        if(nlist[k+1]>y or nlist[k+1]<y):
          ans+=1
        elif(nlist[k+1]==y):
          ans+=2
    print(ans+1)
