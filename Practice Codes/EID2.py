def eidi(a):
  rcount = 0
  for j in range(3):
    for k in range(j+1, 3):
      if(a[j]==a[k] and a[j+3]==a[k+3]):
        rcount+=1
      elif(a[j]>a[k] and a[j+3]>a[k+3]):
        rcount+=1
      elif(a[j]<a[k] and a[j+3]<a[k+3]):
        rcount+=1
  if(rcount==3):
    return "FAIR"
  return "NOT FAIR"
  
test = int(input())
for i in range(test):
  a = list(map(int, input().split()))
  print(eidi(a))
