def kthdiv(n, k):
  rem = n-1
  add = k//rem
  if(k%rem!=0):
    add+=1
    sub = (rem*add)-k
    ans = (n*add)-(sub+1)
  else:
    sub = (rem*add)-k
    ans = (n*add)-(sub+1)
  return ans

test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  print(kthdiv(n, k))
