def bday(n, k, a):
  j = 0
  while(True):
    if(j==n):
      return "yes"
    mine = min(a)
    ind = a.index(mine)
    if((ind-j)%k!=0):
      return "no"
    j+=1
    a[ind] = 1000000001
  
test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  print(bday(n, k, a))
