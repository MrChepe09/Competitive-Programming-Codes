test = int(input())
for i in range(test):
  n = int(input())
  choc = list(map(int, input().split()))
  maxc = max(choc)
  start = choc.index(maxc)
  mid = int(len(choc)/2)
  for j in range(len(choc)-1, 0, -1):
    if(choc[j]==maxc):
      end = j
      break
  ans = ((len(choc))-end)-(mid-start)
  print(max(0, ans))
    
  
