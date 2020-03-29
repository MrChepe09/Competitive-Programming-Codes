def lucky(a):
  l = -1
  for i in range(len(a)):
    if(a.count(a[i])==a[i]):
      l = max(l, a[i])
  return l

aa = list(map(int, input().split()))
print(lucky(aa))
