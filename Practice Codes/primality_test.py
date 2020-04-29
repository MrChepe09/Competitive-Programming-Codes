import math
def primality_test(n):
  if(n>1):
    for j in range(2, int(math.sqrt(n))+1):
      if(n%j==0):
        return "no"
    return "yes"
  else:
    return "no"

test = int(input())
for i in range(test):
  n = int(input())
  print(primality_test(n))
