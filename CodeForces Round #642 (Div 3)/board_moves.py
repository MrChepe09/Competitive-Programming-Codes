def boardmoves(n):
  start = n//2
  count = 0
  while(n!=1):
    count += ((n-1)*4)*start
    start-=1
    n-=2
  return count

test = int(input())
for i in range(test):
  n = int(input())
  print(boardmoves(n))
