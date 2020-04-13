def pisano(n):
  pre, curr = 0, 1
  for i in range(n*n):
    pre, curr = curr, (pre+curr)%n
    if(pre == 0 and curr == 1):
      return i+1
  
def last_digit(f):
  pissano = pisano(10)
  f = f%pissano
  pre, cur = 0, 1
  for i in range(f+1):
    pre, cur = cur, pre+cur
  return((cur-1))

a, b = map(int, input().split())
print((last_digit(b)-last_digit(a-1))%10)
