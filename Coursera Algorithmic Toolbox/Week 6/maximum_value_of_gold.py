def gold(w, n, a):
  dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
  #print(dp)
  for i in range(n+1):
    for j in range(w+1):
      #print(i)
      if(i==0 or j==0):
        dp[i][j] = 0
      elif(a[i-1]<=j):
        dp[i][j] = max(a[i-1]+dp[i-1][j-a[i-1]], dp[i-1][j])
      else:
        dp[i][j] = dp[i-1][j]
  #print(dp)
  return dp[n][w]
        


w, n = map(int, input().split())
a = list(map(int, input().split()))
print(gold(w, n, a))
