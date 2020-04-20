def bus_route(n, d, a):
  p = (d//a[0])
  for j in range(p, 0, -1):
    li = []
    count = 1
    t = a[0]*j
    li.append(t)
    for r in range(1, len(a)):
      z = ((d//a[r])*a[r])
      li.append(z)
      if(z>=(li[r-1])):
        count +=1
    #print(count, t, li)
    if(count==len(a)):
      return t
        


test = int(input())
for i in range(test):
  n, d = map(int, input().split())
  a = list(map(int, input().split()))
  ans =(bus_route(n, d, a))
  print("Case #"+str(i+1)+": "+str(ans))
