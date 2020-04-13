def covid(n, a):
  p = False
  for j in range(len(a)):
    if(a[j]==1 and p==False):
      k = j
      p=True
    elif(a[j]==1 and p):
      if(j-k<6):
        return "NO"
      else:
        k = j
  return "YES"    

test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(covid(n, a))
