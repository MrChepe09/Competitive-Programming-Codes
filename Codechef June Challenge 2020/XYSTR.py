def chefstring(s):
  countx = 0
  j = 0
  while(j<(len(s)-1)):
    if((s[j]=='x' and s[j+1]=='y') or (s[j]=='y' and s[j+1]=='x')):
      countx += 1
      j+=2
    else:
      j+=1
  return countx
      

test = int(input())
for i in range(test):
  s = input()
  print(chefstring(s))
