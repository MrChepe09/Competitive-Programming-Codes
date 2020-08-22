test = int(input())
for i in range(test):
  a, b = input().split()
  cash = [int(j) for j in input().split()]
  print(sum(cash)%(int(b)))
