def chandf(x, y, l, r):
  ans = x|y
  if(min(x, y)==0):
    return 0
  elif(ans<=r and ans>=l):
    return ans
  else:
    


    
test = int(input())
for i in range(test):
  x, y, l, r = map(int, input().split())
  print(chandf(x, y, l, r))
