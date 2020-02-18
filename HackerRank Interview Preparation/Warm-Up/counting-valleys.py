n = int(input())
s = input()
if(s[0] == 'U'):
  sea = 1
else:
  sea = -1
  count = 0
for i in range(1, len(s)):
  if(s[i] == 'U'):
    sea += 1
    if(sea==0):
      count += 1
  elif(s[i] == 'D'):
    sea -= 1

print(count)
