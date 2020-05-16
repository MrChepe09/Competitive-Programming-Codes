def arrswaps(n, a, b, k):
  a.sort()
  b.sort(reverse=True)
  j = 0
  while(k!=0 and j<n):
    if(a[j]<b[j]):
      a[j], b[j] = b[j], a[j]
    else:
      break
    j+=1
    k-=1
  return sum(a)
  

test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  print(arrswaps(n, a, b, k))
