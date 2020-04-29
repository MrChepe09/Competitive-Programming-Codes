def zeroPad(s, count, left=True):
  for i in range(count):
    if(left):
      s = '0'+s
    else:
      s = s+'0'
  return s

def karatsube(x, y):
  x = str(x)
  y = str(y)
  if(len(x)==1 and len(y)==1):
    return int(x)*int(y)
  if(len(x)<len(y)):
    x = zeroPad(x, len(y)-len(x))
  elif(len(x)>len(y)):
    y = zeroPad(y, len(x)-len(y))
  n = len(x)
  j = n//2
  if(n%2!=0):
    j+=1
  Bpad = n-j
  Apad = Bpad*2

  a = int(x[:j])
  b = int(x[j:])
  c = int(y[:j])
  d = int(y[j:])
  #print(a, b, c, d)

  ac = karatsube(a, c)
  bd = karatsube(b, d)
  k = karatsube(a+b, c+d)
  #print(ac, bd, k)
  
  A = int(zeroPad(str(ac), Apad, False))
  B = int(zeroPad(str(k-ac-bd), Bpad, False))
  #print(ac, bd, k, A, B)
  return A+B+bd


test = int(input())
for j in range(test):
  x = int(input())
  y = int(input())
  print(karatsube(x, y))
