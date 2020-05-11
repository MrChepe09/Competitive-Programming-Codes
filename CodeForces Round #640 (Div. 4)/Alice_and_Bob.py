def alicebob(n, a):
  alice = 0
  moves = 1
  yes = 0
  talice = a[0]
  tbob = 0
  bob = 0
  ap = 0
  bp = n-1
  i = 1
  j = n-1
  alice = a[0]
  while(i!=j):
    #print(i, j)
    if(alice>0 and yes==0):
      moves+=1
      while(alice>=0):
        yes = 1
        
        bob += a[j]
        alice-=a[j]
        j-=1
        if(i==j):
          bob+=a[j]
          break
      tbob += bob
      alice = max(0, alice)
    if(bob>0 and yes==0):
      moves+=1
      while(bob>=0):
        yes = 1
        alice += a[i]
        bob-=a[i]
        i+=1
        if(i==j):
          alice+=a[i]
          break
      talice += alice
      bob = max(0, bob)
    yes = 0
  return moves, talice, tbob


test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(alicebob(n, a))
