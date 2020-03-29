def prefix(s, k, x):
  ans = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,'o': 0,'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
  string = 0
  for j in range(len(s)):
    if(ans[s[j]]==x and k==0):
      break
    elif(ans[s[j]]==x and k!=0):
      k -= 1
    else:
      ans[s[j]] += 1
      string += 1
  return(string)
      

test = int(input())
for i in range(test):
  s = input()
  k, x = map(int, input().split())
  print(prefix(s, k, x))
