def rec(s, z, a, b):
  count = int(s[z-2])
  while(s[z]!=')'):
    for p in range(count):
      if(s[z]=='N'):
        a-=1
      elif(s[z]=='S'):
        a+=1
        #print(a)
      elif(s[z]=='E'):
        b+=1
        #print(b)
      elif(s[z]=='W'):
        b-=1
      elif(s[z]=='('):
        h = rec(s, z+1, a, b)
        a = h[0]
        b = h[1]
        z = h[2]
    z+=1
  #print(b, a)
  h = [a, b, z]
  return h

def robotwalk(s):
  a, b = 1, 1
  g = 0
  while(g!=len(s)):
    #4print(s[g], g)
    if(s[g]=='N'):
      a-=1
      #print(b, a)
    elif(s[g]=='S'):
      a+=1
    elif(s[g]=='E'):
      b+=1
    elif(s[g]=='W'):
      b-=1
    elif(s[g]=='('):
      h = rec(s, g+1, a, b)
      a = h[0]
      b = h[1]
      g = h[2]
    #print(b, a, g)
    g+=1
  return [b, a]

test = int(input())
for i in range(test):
  s = input()
  ans = robotwalk(s)
  print(ans)
