def car_fuel(a, f, n):
  count = 0
  curr = 0
  for i in range(1, n+1):
    if(a[i-1]==curr and a[i]>(curr+f)):
      return -1
    elif(a[i+1]>(curr+f)):
      curr = a[i]
      count+=1
  return count

dist = int(input())
fcap = int(input())
n = int(input())
tank = list(map(int, input().split()))
a = [0]
a = a+tank
a.append(dist)
print(car_fuel(a, fcap, n))
