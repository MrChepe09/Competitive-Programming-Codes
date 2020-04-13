def ugcd(n):
  ans = [[1]]
  if(n==1):
    return ans
  elif(n%2==1):
    ans = [[1, 2, n]]
  else:
    ans = [[1, 2]]
  for k in range(1, int(n//2)):
    ans.append([k*2+1, k*2+2])
    
  return ans

test = int(input())
for i in range(test):
  n = int(input())
  p = (ugcd(n))
  print(len(p))
  for j in range(len(p)):
    print(len(p[j]), end=" ")
    print(*p[j])
