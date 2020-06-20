def social(n, k, a):
  count = 0
  ones = [0]
  for j in range(n):
    if(a[j] == '1'):
      ones.append(j)
  ones.append(n-1)
  if(ones==[0, n-1]):
    if(n-1<=k):
      return 1
  print(ones)
  for j in range(1, len(ones)):
    c = ones[j]-ones[j-1]
    if(j==1):
      count+=max(0, (c+2//(k)))
    else:
      count+=max(0, ((c-k)//(k+1)))
    print(c, count)
  return count
  
      

test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  a = input()
  print(social(n, k, a))
