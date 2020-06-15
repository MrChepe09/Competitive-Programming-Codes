def vacation(n, a):
  dp = [0]*3

  
  for i in range(3):
    dp[i] = a[0][i]

    
  for i in range(1, n):
    temp = [0]*3
    for j in range(3):
      for k in range(3):
        if(j!=k):
          temp[j] = max(temp[j], dp[k]+a[i][j])
    dp = temp
  return max(dp)
    


n = int(input())
a = []
for i in range(n):
  g = list(map(int, input().split()))
  a.append(g)
print(vacation(n, a))
