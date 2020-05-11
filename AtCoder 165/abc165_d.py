import math
def floorm(a, b, n):
  ans = math.floor((a*n)/b) - a*(math.floor(n/b))
  return ans

  
a, b, n = map(int, input().split())
if(b>n):
  print(floorm(a, b, n))
else:
  print(floorm(a, b, b-1))
