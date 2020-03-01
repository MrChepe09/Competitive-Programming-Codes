def find(a, b):
  for i in range(len(a)):
    if(a[i] not in b):
      return(a[i])
x = list(map(int, input().split()))
y = list(map(int, input().split()))
if(len(x)>len(y)):
  print(find(x, y))
else:
  print(find(y, x))
