n = int(input())
socks = [int(i) for i in input().split()]
pairs = []
count = 0
for i in range(len(socks)):
  if(socks[i] in pairs):
    pairs.remove(socks[i])
    count = count + 1
  else:
    pairs.append(socks[i])
print(count)
