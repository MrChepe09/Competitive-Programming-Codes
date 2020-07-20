def fashionablee(n):
  if(n%4==0):
    return 'YES'
  return 'NO'

test = int(input())
for i in range(test):
  n = int(input())
  print(fashionablee(n))
