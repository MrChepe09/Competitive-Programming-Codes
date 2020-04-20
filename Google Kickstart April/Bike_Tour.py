def biketour(n, a):
  count = 0
  for j in range(1, n-1):
    if(a[j]>a[j-1] and a[j]>a[j+1]):
      count+=1
  return count
test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  ans = biketour(n, a)
  print("Case #"+str(i+1)+": "+str(ans))
