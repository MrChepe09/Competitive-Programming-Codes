test_cases = int(input())
for i in range(test_cases):
  y = [int(i) for i in input().split()]
  if y[1] <= 2:
    print("NO")
  else:
    print("YES")
