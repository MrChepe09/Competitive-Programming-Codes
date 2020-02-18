test_cases = int(input())
for i in range(test_cases):
  ans = ['YES']
  a, b = input().split()
  a = int(a)
  b = int(b)
  for d in range(a):
    ans.append(0)
  dup = [int(j) for j in input().split()]
  coins = dup.copy()
  coins.reverse()

#------------------
  t = 0
  while(t<len(coins) and b>0):
    if(b>coins[t]):
      if(b%coins[t]==0):
        count = int(b/coins[t] - 1)
        b = b - (count*coins[t])
      else:
        count = int(b/coins[t])
        b = b - (count*coins[t])
      ans[dup.index(coins[t]) + 1] += count
    elif(b<coins[t]):
      b = b - coins[t]
      ans[dup.index(coins[t]) + 1] += 1
      break
    else:
      t = t+1
#--------------------


  if(b>0):
    print("NO")
  else:
    print(*ans)
