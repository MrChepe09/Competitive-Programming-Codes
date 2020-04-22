def problemD(n, k, a):


test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  print(problemD(n, k, a))
