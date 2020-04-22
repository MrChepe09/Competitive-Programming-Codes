def problemA(n):
  a = 3
  c = 2
  while(n%a!=0):
    b = 2**c
    a+=b
    c+=1
  return int(n/a)

test = int(input())
for i in range(test):
  n = int(input())
  print(problemA(n))
