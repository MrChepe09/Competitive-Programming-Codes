import math
def chefdenom(s, n):
  count = 0
  if(s%2==1):
    count+=1
    s-=1
  count += int(math.ceil(s/n))
  return count
    


test = int(input())
for i in range(test):
  s, n = map(int, input().split())
  print(chefdenom(s, n))
