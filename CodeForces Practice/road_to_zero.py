def roadzero(a, b, ca, cb):
  cost = 0
  if(a>b):
    a, b = b, a
  cost += ca*(b-a)
  if(2*ca<cb):
    cost += (a*(2*ca))
  else:
    cost += (a*cb)
  return cost
  
test = int(input())
for i in range(test):
  a, b = map(int, input().split())
  costa, costb = map(int, input().split())
  print(roadzero(a, b, costa, costb))
