def car_fuel(a, f, n):
  count = 0
  curr = 0
  for i in range(1, n+2):
    if(a[i]>(a[i-1]+f)):
      return -1
    elif(a[i]>(curr+f)):
      curr = a[i-1]
      count+=1
    #print(curr, count)
  return count

dist = int(input())
fcap = int(input())
n = int(input())
tank = list(map(int, input().split()))
a = [0]
a = a+tank
a.append(dist)
print(car_fuel(a, fcap, n))
