def nrepeat(n, a):
  return (len(list(set(a))))


test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(nrepeat(n, a))
