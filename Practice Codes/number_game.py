def numbergame(n):
  if(n==1):
    return "FastestFinger"
  if(n%2==1):
    return "Ashishgup"
  if(n%2==0):
    count = 0
    while(n%2==0):
      count += 1
      n = n//2
    if(count%2==1):
      return "FastestFinger"
    else:
      return "Ashishgup"

test = int(input())
for i in range(test):
  n = int(input())
  print(numbergame(n))
