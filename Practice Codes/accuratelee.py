def accuratelee(n, s):
  i = 0
  s = list(s)
  g = []
  prev = None
  for i in range(n):
    if(prev=='1' and s[i]=='0'):
      g.append('0')
    else:
      prev = s[i]
      g.append(s[i])
    
      
  return ''.join(g)

test = int(input())
for i in range(test):
  n = int(input())
  s = input()
  print(accuratelee(n, s))
