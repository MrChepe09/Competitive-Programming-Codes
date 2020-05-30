def lostweek(a):
  mul = a[-1]
  for i in range(5):
    a[i] *= mul
  a[-1] = 0
  if(sum(a)<=120):
    return 'No'
  return "Yes"


test = int(input())
for i in range(test):
  a = list(map(int, input().split()))
  print(lostweek(a))
