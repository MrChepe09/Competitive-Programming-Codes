def cheficecream(n, a):
  coins = {5: 0, 10: 0}
  for i in range(n):
    if(a[i]==5):
      coins[5] += 1
    elif(a[i] == 10):
      coins[10] += 1
      if(coins[5]==0):
        return "NO"
      else:
        coins[5]-=1
    elif(a[i] == 15):
      if(coins[10]==0 and coins[5]<2):
        return "NO"
      elif(coins[10]!= 0):
        coins[10] -= 1
      elif(coins[10]==0 and coins[5]>=2):
        coins[5] -= 2
  return "YES"

test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(cheficecream(n, a))
