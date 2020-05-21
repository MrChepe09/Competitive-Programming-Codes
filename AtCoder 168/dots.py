def dots(k, s):
  if(len(s)<=k):
    return s
  else:
    return s[:k]+'...'

k = int(input())
s = input()
print(dots(k, s))
