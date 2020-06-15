def troublesort(a, b):
  if(a==sorted(a)):
    return "Yes"
  else:
    c1 = b.count(1)
    c2 = b.count(0)
    if(c1!=0 and c2!=0):
      return "Yes"
    else:
      return "No"


test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  print(troublesort(a, b))
  
