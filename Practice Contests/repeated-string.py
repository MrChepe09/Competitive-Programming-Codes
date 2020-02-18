s = input()
n = int(input())
count = s.count('a')
lg = len(s)
if(n==1):
  pass
elif(n%lg==0):
  p = int(n/lg)
  count = count * p
else:
  p = int(n/lg)
  count = count * p
  z = n - (p*lg)
  for i in range(z):
    if(s[i] == 'a'):
      count+= 1
print(count)
