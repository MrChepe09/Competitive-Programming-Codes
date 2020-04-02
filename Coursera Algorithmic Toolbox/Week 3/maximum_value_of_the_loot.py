def knapsack(n, v, wg, a):
  wg1 = [x for _,x in sorted(zip(a,wg))]
  v1 = [x for _,x in sorted(zip(a,v))]
  a.sort()
  j = len(a)-1
  total = 0
  while(n>0 and j>=0):
    if(wg1[j]<=n):
      n-=wg1[j]
      total += v1[j]
    else:
      t = float(n/wg1[j])
      n=0
      total += (v1[j]*t)
    j-=1
  return float(int(total*10000))/10000

n, w = map(int, input().split())
a = [0]*n
v = [0]*n
wg = [0]*n
for i in range(n):
  p, q = map(int, input().split())
  v[i] = p
  wg[i]= q
  a[i] = (p/q)
print(knapsack(w, v, wg, a))
