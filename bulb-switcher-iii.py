a = list(map(int, input().split()))
ans = [0]*len(a)
maxi = 0
r = 0
for i in a:
  ans[i-1] = 1
  maxi = max(maxi, i)
  if(0 not in ans[0:maxi]):
    r += 1
  print(ans[0:maxi])
print(r)
