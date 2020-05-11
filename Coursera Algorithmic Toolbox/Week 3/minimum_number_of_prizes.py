def prizes(n):
  a = [1]
  j = 0
  start = 1
  while(n>0):
    if(n>a[j]):
      start += 1
      a.append(start)
      n-=start
    elif(n<=a[j]):
      a[j]+=n
      n = 0
    j+=1
  return a

n = int(input())
ans = prizes(n-1)
print(len(ans))
print(*ans)
