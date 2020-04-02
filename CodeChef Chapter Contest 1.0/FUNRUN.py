def race(a, b):
  if(a[-1]>b[-1] or a[-1]<b[-1]):
    return "YES"
  else:
    return "NO"
    
test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  a.sort()
  b.sort()
  print(race(a, b))
