def sortvs(n, m, nlist, mlist):
  bolt = [False]*(n+1)
  ans = [0]*(n+1)
  for j in range(1, n+1):
    ans[j] = nlist[j-1]
  swaps = 0
  for k in range(1, len(ans)):
    if(bolt[k] == False):
      bolt[k] = True
      if(k==ans[k]):
        continue
      else:
        ci = ans[k]
        while(not bolt[ci]):
          bolt[ci] = True
          nex = ans[ci]
          ci = nex
          swaps+=1
  return swaps

test = int(input())
for i in range(test):
  n, m= map(int, input().split())
  nlist = list(map(int, input().split()))
  mlist = []
  for j in range(m):
    xy = list(map(int, input().split()))
    mlist.append(xy)
  print(sortvs(n, m, nlist, mlist))
