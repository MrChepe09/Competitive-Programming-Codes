test_cases = int(input())
for i in range(test_cases):
  n = [int(i) for i in input().split()]
  a = [int(i) for i in input().split()]
  if sum(a)<=n[1]:
    print('Yes')
  else:
    print('No')
