def lcs2(n, a, m, b, o, c):
  dp = [[[0 for _ in range(o+1)] for _ in range(m+1)] for _ in range(n+1)]
  for i in range(0, n+1):
    for j in range(0, m+1):
      for k in range(0, o+1):
        if(i==0 or j==0 or k==0):
          dp[i][j][k] = 0
        elif(a[i-1]==b[j-1] and a[i-1] == c[k-1]):
          dp[i][j][k] = dp[i-1][j-1][k-1] + 1
        else:
          dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
  return dp[n][m][o]

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
o = int(input())
c = list(map(int, input().split()))
print(lcs2(n, a, m, b, o, c))
