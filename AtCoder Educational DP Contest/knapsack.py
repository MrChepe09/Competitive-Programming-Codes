def knapsack(n, W, w, v):
  dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
  for i in range(n+1):
    for j in range(W+1):
      if(i==0 or j==0):
        dp[i][j] = 0
      elif(w[i-1]<=j):
        dp[i][j] = max(v[i-1]+dp[i-1][j-w[i-1]], dp[i-1][j])
      else:
        dp[i][j] = dp[i-1][j]
  return dp[n][W]


n, W = map(int, input().split())
we = []
va = []
for i in range(n):
  w, v = map(int, input().split())
  we.append(w)
  va.append(v)
print(knapsack(n, W, we, va))
