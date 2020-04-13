def depth(i, s):
  a = []
  t = 0
  s = s+'0'
  for j in range(len(s)-1):
    n = (int(s[j])-t)
    a.append('('*n)
    t+=n
    a.append(s[j])
    m = max(0, int(s[j])-int(s[j+1]))
    a.append(')'*m)
    t-=m
  z = ''.join(a)
  ans = ''.join(z.split())
  return "Case #"+str(i+1)+": "+str(ans)


test = int(input())
for i in range(test):
  s = input()
  print(depth(i, s))
