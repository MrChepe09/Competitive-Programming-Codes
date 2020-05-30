def minsquare(a, b):
  mini = min(a, b)*2
  if(a==b):
    return (a+b)**2
  elif(max(a, b)>mini):
    return max(a, b)**2
  elif(max(a, b)<=mini):
    return mini**2
  
test = int(input())
for i in range(test):
  a, b = map(int, input().split())
  print(minsquare(a, b))
