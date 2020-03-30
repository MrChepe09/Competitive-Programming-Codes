def change(n):
  coins = [10, 5, 1]
  i = 0
  count = 0
  while(n>0):
    if(n>=coins[i]):
      n -= coins[i]
      count += 1
    else:
      i += 1
  return count

n = int(input())
print(change(n))
