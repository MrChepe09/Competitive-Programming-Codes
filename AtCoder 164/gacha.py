n = int(input())
a = []
count = 0
for i in range(n):
  item = input()
  a.append(item)
print(len(list(set(a))))
