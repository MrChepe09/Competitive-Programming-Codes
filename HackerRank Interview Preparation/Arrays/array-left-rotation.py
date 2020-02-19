n, d = input().split()
ans = []
n = int(n)
d = int(d)
a = list(map(int, input().split()))
while(n>=0):
  if(d>len(a)-1):
    d = 0
  else:
    ans.append(a[d])
    d+=1
  n-=1
print(ans)
  
  
