def gcd(a, b):
  if(b==0):
   return a
  else:
    return gcd(b, a%b)

test = int(input())
for i in range(test):
  a, b = map(int, input().split())
  print(gcd(a, b))
