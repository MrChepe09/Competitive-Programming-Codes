def ks1(n, a):
  ans = {0: [1, 0]}
  pre = [0]*(n+1)
  total = 0
  for j in range(1, n+1):
    pre[j] = a[j-1]^pre[j-1]
    if(pre[j] not in ans):
      ans[pre[j]] = [1, j]
    else:
      if(ans[pre[j]][0]>0):
        count = ans[pre[j]][0]
        sump = ans[pre[j]][1]  
        total += ((count*j)-count-sump)
      ans[pre[j]][0]+=1
      ans[pre[j]][1]+=(j)
      print(total)
  print(ans, pre)
  return total


test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(ks1(n, a))
