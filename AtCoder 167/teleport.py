def teleport(n, k, a):
  start = 1
  done = []
  p = k
  for i in range(k):
    done.append(start)
    start = a[start-1]
    if(start in done):
      ind = done.index(start)
      break
  dif = ind
  p-=dif
  p = p%(len(done)-dif)
  #print(p, dif, ind)
  return done[ind+p]

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(teleport(n, k, a))
