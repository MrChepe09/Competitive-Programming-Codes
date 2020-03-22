nums = list(map(int, input().split()))
index = list(map(int, input().split()))
ans = []
for i in range(len(index)):
  ans.insert(index[i], nums[i])
print(ans)

