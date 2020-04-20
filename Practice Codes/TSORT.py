def dsort(a):
  a.sort()
  return a

t = int(input())
a = []
for i in range(t):
  n = int(input())
  a.append(n)
p = (dsort(a))
for i in range(t):
  print(a[i])
