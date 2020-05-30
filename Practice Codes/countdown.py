def countdown(n, k, a):
  g = 0
  count = 0
  tog = 0
  for g in range(len(a)):
    if(a[g]==k):
      tog = k
      p = g
    elif(a[g]==tog-1):
      tog-=1
    elif(a[g]>k):
      tog = 0

    if(tog==1):
      count+=1
      tog = 0
  return count

test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  z = countdown(n, k, a)
  print("Case #"+str(i+1)+": "+str(z))
