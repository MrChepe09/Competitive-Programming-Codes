def teamcomp(n, a):
  if(n==1):
    return 0
  fre = {}
  same = 0
  unique = 0
  for i in a:
    if(i in fre):
      fre[i] += 1
      same = max(same, fre[i])
    else:
      fre[i] = 1
      unique += 1
      same = max(same, fre[i])
  if(same==unique-1):
    return same
  else:
    val1 = min(same, unique-1)
    val2 = min(same-1, unique)
    return max(val1, val2)
      
  
    
  
test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(teamcomp(n, a))
