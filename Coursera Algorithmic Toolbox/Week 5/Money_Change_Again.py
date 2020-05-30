def moneychange(n, coins):
  dp = [0]*(n+1)
  for j in range(1, n+1):
    mini = 100000
    for i in range(1, len(coins)+1):
      if(j>=coins[i-1]):
        mini = min(mini, 1+dp[j-coins[i-1]])
    dp[j] = mini
  return dp[n]
  
n = int(input())
coins = [1, 3, 4]
print(moneychange(n, coins))
