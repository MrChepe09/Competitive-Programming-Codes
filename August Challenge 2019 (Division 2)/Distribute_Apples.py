test_cases = int(input())
for i in range(test_cases):
  y = [int(i) for i in input().split()]
  if y[1] == 1:
    print("NO")
  elif y[0] == y[1]:
    print("YES")
  else:
    square = y[1]*y[1]
    if y[0]%square==0:
      print("NO")
    else:
      print("YES")
