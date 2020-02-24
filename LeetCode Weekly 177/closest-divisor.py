n = int(input())
num1 = n+1
num2 = n+2
ans = []
maxdif1 = num1
maxdif2 = num2
for i in range(1, int(num1/2)):
  if(num1/i == int(num1/i)):
    if(abs(i-int(num1/i))<maxdif1):
      maxdif1 = abs(i-int(num1/i))
      x = i
      y = int(num1/i)
for i in range(1, int(num2/2)):
  if(num2/i == int(num2/i)):
    if(abs(i-int(num2/i))<maxdif2):
      maxdif2 = abs(i-int(num2/i))
      r = i
      t = int(num2/i)
if(maxdif1>maxdif2):
  ans.append(r)
  ans.append(t)
else:
  ans.append(x)
  ans.append(y)
print(ans)
  
