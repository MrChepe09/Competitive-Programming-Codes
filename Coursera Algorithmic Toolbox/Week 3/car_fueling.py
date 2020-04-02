def car_fuel(a, f):
  count = 0
  curr = 0
  for i in range(len(a)-1):
    if(a[i+1]<f-curr):
      
  



dist = int(input())
fcap = int(input())
n = int(input())
tank = list(map(int, input().split()))
a = [0]
a = a+tank
a.append(dist)
print(car_fuel(a, fcap))
