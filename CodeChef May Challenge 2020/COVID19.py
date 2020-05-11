def covid19(n, a):
  maxi = 0
  mini = 20
  for j in range(n):
    count = 1
    curr = a[j]
    for k in range(j+1, n):
      if(abs(a[k]-curr)<=2):
        count+=1
        curr = a[k]
      else:
        break
    curr = a[j]
    for k in range(j-1, -1, -1):
      if(abs(a[k]-curr)<=2):
        count+=1
        curr = a[k]
      else:
        break
    mini = min(mini, count)
    maxi = max(maxi, count)
  return str(mini)+" "+str(maxi)

test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(covid19(n, a))
