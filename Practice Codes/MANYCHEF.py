def signboard(s):
  arr = []
  s = list(s)
  for i in range(len(s)-4, -1, -1):
    if((s[i]=='C' or s[i]=='?') and (s[i+1]=='H' or s[i+1]=='?') and (s[i+2]=='E' or s[i+2]=='?') and (s[i+3]=='F' or s[i+3]=='?')):
      s[i] = 'C'
      s[i+1] = 'H'
      s[i+2] = 'E'
      s[i+3] = 'F'
  for i in range(len(s)):
    if(s[i] == '?'):
      s[i] = 'A'
  return ''.join(s)

test = int(input())
for j in range(test):
  s = input()
  print(signboard(s))
