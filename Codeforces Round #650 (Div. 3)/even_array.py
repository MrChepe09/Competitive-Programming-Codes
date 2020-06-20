def evenarr(n, a):
  even = 0
  odd = 0
  for i in range(len(a)):
    if(a[i]%2 != i%2):
      if(a[i]%2==0):
        odd += 1
      else:
        even += 1
  if(even==odd):
    return even
  else:
    return -1


test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(evenarr(n, a))
