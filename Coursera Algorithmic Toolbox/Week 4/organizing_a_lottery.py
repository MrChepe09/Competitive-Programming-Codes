def lottery(seg, poi):
  gg = []
  for i in poi:
    count = 0
    for j in seg:
      if(i>=j[0] and i<=j[1]):
        count+=1
    gg.append(count)
  return gg


s, p = map(int, input().split())
seg = []
for i in range(s):
  a = list(map(int, input().split()))
  seg.append(a)
poi = list(map(int, input().split()))
ans = lottery(seg, poi)
print(*ans)
