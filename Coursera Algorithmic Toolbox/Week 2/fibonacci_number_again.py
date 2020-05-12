def pisano(n):
  pre, curr = 0, 1
  for i in range(n*n):
    pre, curr = curr, (pre+curr)%n
    if(pre == 0 and curr == 1):
      return i+1
  
def last_digit(f, n):
  pissano = pisano(n)
  f = f%pissano
  if(f<=1):
    return f
  pre, cur = 0, 1
  for i in range(f-1):
    pre, cur = cur, pre+cur
  return(cur%n)

f, n = map(int, input().split())
print(last_digit(f, n))
