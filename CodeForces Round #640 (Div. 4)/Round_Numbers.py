def roundnumber(n):
  n = str(n)
  ans = []
  for j in range(len(n)):
    dig = []
    if(n[j]!='0'):
      dig.append(n[j])
      zero = ['0']*(len(n)-(j+1))
      dig += zero
      st = ''.join(dig)
      ans.append(int(st))
  return ans

test = int(input())
for i in range(test):
  n = int(input())
  z = roundnumber(n)
  print(len(z))
  print(*z)
