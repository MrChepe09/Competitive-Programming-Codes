def strange(x, k):
  count = 0
  while(x%2==0):
    x /= 2
    count += 1

  for j in range(3, int(x**0.5)+1, 2):
    while(x%j==0):
      x /= j
      count+=1
        
  if(x>=2):
    count+=1

  if(k<=count):
    return 1
  else:
    return 0

test = int(input())
for i in range(test):
  x, k = map(int, input().split())
  print(strange(x, k))
