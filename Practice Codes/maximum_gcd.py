def gcdpair(n):
  while(n%2!=0):
    n-=1
  return n//2


test = int(input())
for i in range(test):
  n = int(input())
  print(gcdpair(n))
