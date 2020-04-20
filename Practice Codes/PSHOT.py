def goal(n, s):
  rema = n
  remb = n
  scorea = 0
  scoreb = 0
  for j in range(len(s)):
    if((scorea-scoreb)>remb or (scoreb-scorea)>rema):
      return j
    elif(j%2==0):
      if(s[j]=='1'):
        scorea+=1
      rema-=1
    elif(j%2==1):
      if(s[j]=='1'):
        scoreb+=1
      remb-=1
  return j+1

test = int(input())
for i in range(test):
  n = int(input())
  s = input()
  print(goal(n, s))
