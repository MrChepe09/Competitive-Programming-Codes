def percent(n):
  start = 100
  count = 0
  while(start<n):
    interest = int(start * (1/100))
    count+=1
    start += interest
    #print(start)
  return count


n = int(input())
print(percent(n))
