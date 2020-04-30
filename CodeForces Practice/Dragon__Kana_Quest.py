def dragon(h, a, b):
  while(a>0 or b>0):
    if(h<=0):
      return 'YES'
    aspell = (h//2)+10
    bspell = h-10
    #print(aspell, h)
    if(aspell>h):
      #print(b, h)
      h-=(10*b)
      b=0
      break
    #print(h)
    if(a!=0):
      a-=1
      h = aspell
    else:
      b-=1
      h = bspell
  if(h<=0):
      return 'YES'
  else:
    return "NO"
    

test = int(input())
for i in range(test):
  h, a, b = map(int, input().split())
  print(dragon(h, a, b))
