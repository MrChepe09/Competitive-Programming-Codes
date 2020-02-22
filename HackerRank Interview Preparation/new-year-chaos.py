test = int(input())
for i in range(test):
  n = int(input())
  bribe = 0
  person = list(map(int, input().split()))
  count = 0
  for j in range(n):
    if(person[j]-(j+1)>2):
      count+=1
      break

  if(count>0):
    print("Too chaotic")
  else:
    for j in range(n):
      z = (max(person)-(person.index(max(person))+1))
      bribe += z
      person.remove(max(person))
    print(bribe)
    
