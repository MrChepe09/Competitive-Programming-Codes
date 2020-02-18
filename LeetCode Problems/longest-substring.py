s = input()
maxi = 0
for i in range(len(s)):
  ans = []
  ans.append(s[i])
  for j in range(i+1, len(s)):
    if(s[j] not in ans):
      ans.append(s[j])
    else:
      break
  maxi = max(maxi, len(ans))
print(maxi)
