def simpairs(n, a):
  evens = 0
  odds = 0
  g = list(a)
  g.sort()
  seq = 0
  for i in range(n-1):
    if(g[i+1]-g[i]==1):
      seq+=1
      
  for i in a:
    if(i%2==0):
      evens += 1
    else:
      odds += 1
      
  if(evens%2==0 and odds%2==0):
    return "YES"
  elif(evens%2!=0 and odds%2!=0 and seq>=1):
    return "YES"
  return "NO"
  

test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(simpairs(n, a))
