def trace(i, a, n):
  t = 0
  z , b = 0, 0
  for k in range(n):
    t+= a[k][k]
  for k in range(n):
    g = []
    h = []
    for d in range(n):
      if(a[k][d] in g):
        z+=1
        break
      g.append(a[k][d])
  for k in range(n):
    h = []
    for d in range(n):
      if(a[d][k] in h):
        b+=1
        break
      h.append(a[d][k])
  return "Case #"+str(i+1)+": "+str(t)+" "+str(z)+" "+str(b)

test = int(input())
for i in range(test):
  a = []
  n = int(input())
  for j in range(n):
    ai = list(map(int, input().split()))
    a.append(ai)
  print(trace(i, a, n))
  
