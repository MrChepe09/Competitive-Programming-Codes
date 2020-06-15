def chefprice(n, k, a):
  count = 0
  for j in range(n):
    if(a[j] > k):
      count += (a[j]-k)
  return count

test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  print(chefprice(n, k, a))
