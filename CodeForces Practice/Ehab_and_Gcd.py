def gcdlcm(n):
  a = 1
  b = n - 1
  ans = str(a)+" "+str(b)
  return ans

test = int(input())
for i in range(test):
  n = int(input())
  print(gcdlcm(n))
