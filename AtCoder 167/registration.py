def registration(s, t):
  for i in range(len(s)):
    if(s[i]!=t[i]):
      return "No"
  return "Yes"

s = input()
t = input()
print(registration(s, t))
