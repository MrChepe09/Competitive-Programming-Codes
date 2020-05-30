def weirdwalk(n, a, b):
  alice = 0
  bob = 0
  total = 0
  for i in range(n):
    if((a[i]==b[i]) and (alice==bob)):
      total+=a[i]
    alice+=a[i]
    bob+=b[i]
  return total

test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  print(weirdwalk(n, a, b))
