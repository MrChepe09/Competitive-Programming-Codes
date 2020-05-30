def chefship(s):
  count = 0
  for i in range(1, len(s)-2, 2):
    if(s[:(i+1)//2] == s[(i+1)//2:i+1]):
      if(s[i+1: (len(s)+i+1)//2] == s[(len(s)+i+1)//2:]):
        count+=1
  return count


test = int(input())
for i in range(test):
  s = input()
  print(chefship(s))
