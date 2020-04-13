def parent(n, arr):
  ans = []
  for t in range(n):
    ans.append((arr[t][0], arr[t][1], t))
    ans.sort()
    ce = 0
    je = 0
    arr2 = []
    for s, e, z in ans:
      if(s<ce and s<je):
        return "IMPOSSIBLE"
      if(s>=ce):
        arr2.append(('C', z))
        ce = e
      else:
        arr2.append(('J', z))
        je = e
    pp = ""
    for c, z in sorted(arr2, key=lambda x:x[1]):
      pp+=c
  return pp


test = int(input())
for i in range(test):
  n = int(input())
  arr = []
  for j in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
  d = (parent(n, arr))
  print('Case #'+str(i+1)+": "+str(d))
    
    
      
