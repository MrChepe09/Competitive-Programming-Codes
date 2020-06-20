def sub(s):
  a = []
  for i in range(len(s)):
    if(i%2==0):
      a.append(s[i])
  if(len(s)%2==0):
    a.append(s[-1])
  return ''.join(a)


test = int(input())
for i in range(test):
  s = input()
  print(sub(s))
