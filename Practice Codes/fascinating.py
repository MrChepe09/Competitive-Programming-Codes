t=int(input())
for i in range(t):
  count = 0
  a = int(input())
  b = str(a*2)
  c = str(a*3)
  a = str(a)
  a = a + b + c
  print(a)
  for j in range(1, 10):
    if str(j) in a:
      count = count + 1
  if count == 9:
    print(1)
  else:
    print(0)
      
