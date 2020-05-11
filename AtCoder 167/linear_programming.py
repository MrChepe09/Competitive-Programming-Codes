def linear(a, b, c, k):
  count = 0
  if(k>a):
    count+=a
    k-=a
    if(k>b):
      k-=b
      if(k>c):
        count-=c
      else:
        count-=k
    return count
  else:
    return k

a, b, c, k = map(int, input().split())
print(linear(a, b, c, k))
