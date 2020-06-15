import sys
n = int(input())
a = list(map(int, input().split()))

dp = [sys.maxsize]*n
dp[0] = 0
for i in range(n):
  for j in range(i+1, i+2+1):
    if(j<n):
      dp[j] = min(dp[j], dp[i]+abs(a[i]-a[j]))
print(dp[n-1])
