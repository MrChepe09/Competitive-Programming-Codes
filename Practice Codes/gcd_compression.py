def gcdcompress(n, a):
  odds = 0
  evens = 0
  for i in a:
    if(i%2==0):
      evens += 1
    else:
      odds += 1
  
    


test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(gcdcompress(n, a))
