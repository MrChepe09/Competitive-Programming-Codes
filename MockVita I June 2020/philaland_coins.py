def mincoins(n):
  count = 1
  g = 2
  while(n//g>0):
    count += 1
    g *= 2
  return count

test = int(input())
for i in range(test):
  n = int(input())
  print(mincoins(n))
