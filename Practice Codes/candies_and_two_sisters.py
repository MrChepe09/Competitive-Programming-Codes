def candies(n):
  if(n%2==0):
    return int((n/2)-1)
  else:
    return int(n/2)

test = int(input())
for i in range(test):
  n = int(input())
  print(candies(n))
