def sameparity(a, b):
  arr = []
  count = 0
  if(a==b):
    arr = [1]*a
    return arr
  if(a%2==0):
    if(b%2==0):
      while(b!=1):
        arr.append(1)
        b-=1
        count +=1
        if(count==a):
          return "NO"
    else:
      while(b!=1):
        arr.append(2)
        b-=1
        count +=2
        if(count==a):
          return "NO"
    arr.append(a-count)
      
  else:
    if(b%2==0):
      return "NO"
    else:
      while(b!=1):
        arr.append(1)
        b-=1
        count +=1
        if(count==a):
          return "NO"
    arr.append(a-count)
      
      
  return arr
    

test = int(input())
for i in range(test):
  a, b = map(int, input().split())
  z = sameparity(a, b)
  if(z=='NO'):
    print(z)
  else:
    print("YES")
    print(*z)
