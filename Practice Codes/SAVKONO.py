def naruto(n, z, a):
  start = 0
  count = 0
  while(z>0):
    #print(z)
    if(start==n):
      start = 0
    if(a[0]==0):
      return "Evacuate"
    z -= a[start]
    a[start] = a[start]//2
    start += 1
    count += 1
  return count
    


test = int(input())
for i in range(test):
  n, z = map(int, input().split())
  a = list(map(int, input().split()))
  a.sort(reverse=True)
  print(naruto(n, z, a))
