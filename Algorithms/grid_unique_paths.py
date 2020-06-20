def uniquepath(m, n):
  if(dp[m][n] != 0):
    return dp[m][n]
  if(m == 1 or n==1):
    dp[m][n] = 1
    return dp[m][n]
  #print(dp)
  dp[m][n] = uniquepath(m-1, n) + uniquepath(m, n-1)
  return dp[m][n]



test = int(input())
for i in range(test):
  m = int(input())
  n = int(input())
  dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
  print(uniquepath(m, n))
  print(dp)
