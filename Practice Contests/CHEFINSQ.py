test_cases = int(input())
for i in range(test_cases):
  n = [int(i) for i in input().split()]
  a = [int(i) for i in input().split()]
  a.sort()
  minimum = 0
  count = 1
  for j in range(n[1]):
    minimum += a[j]
  for p in range(n[1], n[0]):
    y = (minimum - a[p-1]) + a[p]
    if(minimum == y):
      count += 1
    else:
      break
  print(count)
