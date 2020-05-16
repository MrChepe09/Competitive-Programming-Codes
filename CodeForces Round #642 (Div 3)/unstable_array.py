def unsarr(n, m):
  if(n==1):
    return 0
  elif(n==2):
    return m
  else:
    return m*2
    


test = int(input())
for i in range(test):
  n, m = map(int, input().split())
  print(unsarr(n, m))
