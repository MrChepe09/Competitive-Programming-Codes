def jain(a):
  v = ['a', 'e', 'i', 'o', 'u']
  an = 0
  for k in range(len(a)):
    for g in range(k+1, len(a)):
      z = a[k]+a[g]
      count = 0
      for w in v:
        if(w in z):
          count+=1
      if(count==5):
        an+=1
  return an

test = int(input())
for i in range(test):
  n = int(input())
  ans = []
  for j in range(n):
    p = input()
    ans.append(p)
  print(jain(ans))
