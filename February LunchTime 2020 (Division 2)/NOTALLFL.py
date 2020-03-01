test = int(input())
for i in range(test):
  n, z = map(int, input().split())
  flavor = list(map(int, input().split()))
  maxi = 0
  length = 0
  lis = []
  done = []
  for j in range(0, n):
    if(len(done)<z-1 and flavor[j] not in done):
      done.append(flavor[j])
      lis.append(flavor[j])
      length += 1
    elif(flavor[j] in done):
      length += 1
      lis.append(flavor[j])
    else:
      #print(lis)
      maxi = max(maxi, len(lis))
      lis.append(flavor[j])
      while(len(done)==z-1):
        g = lis[0]
        lis.remove(lis[0])
        if g not in lis:
          done.remove(g)
      done.append(flavor[j])
  #print(lis)
  maxi = max(maxi, len(lis))
    
  print(maxi)
        
        
        
        
        
