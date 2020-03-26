def lcm(a, b):
  for j in range(1, b):
    if(a==0 or b==0):
      return 0
    if((a*j)%b==0):
      return a*j
  return a*b

test = int(input())
for i in range(test):
  a, b = map(int, input().split())
  if(a<b):
    print(lcm(a, b))
  else:
    print(lcm(b, a))
