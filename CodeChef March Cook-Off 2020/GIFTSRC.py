test = int(input())
for i in range(test):
  n = int(input())
  seq = input()
  ans = [0, 0]
  if(seq[0]=='L'):
    ans[0] -= 1
  elif(seq[0]=='R'):
    ans[0] += 1
  elif(seq[0]=='U'):
    ans[1] += 1
  elif(seq[0]=='D'):
    ans[1] -= 1
  for j in range(1, len(seq)):
    if(seq[j] == 'L' and seq[j-1] != 'L' and seq[j-1] != 'R'):
      ans[0] -= 1
    elif(seq[j] == 'R' and seq[j-1] != 'R' and seq[j-1] != 'L'):
      ans[0] += 1
    elif(seq[j] == 'U' and seq[j-1] != 'U' and seq[j-1] != 'D'):
      ans[1] += 1
    elif(seq[j] == 'D' and seq[j-1] != 'D' and seq[j-1] != 'U'):
      ans[1] -= 1
  print(ans[0], ans[1])
