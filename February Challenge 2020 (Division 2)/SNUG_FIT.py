test_cases = int(input())
for i in range(test_cases):
  count = 0
  n = int(input())
  a = [int(j) for j in input().split()]
  b = [int(j) for j in input().split()]
  a.sort()
  b.sort()
  for j in range(len(a)):
    if (a[j] < b[j]):
      count += a[j]
    else:
      count += b[j]
  print(count)
