def jerryw(n):
  while(n%2==0):
    n = n//2
  return n
  
def tomjerry(n):
  if(n==1):
    return 0
  count = 0
  if(n%2==1):
    return (n-1)//2
  else:
    return jerryw(n)//2

test = int(input())
for i in range(test):
  n = int(input())
  print(tomjerry(n))

  
