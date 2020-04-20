def rev_str(s):
    ans = []
    g = []
    for j in range(len(s)-1, -1, -1):
       if(s[j] == '.'):
         for k in reversed(g):
           ans.append(k)
         ans.append('.')
         g = []
       else:
         g.append(s[j])
    for k in reversed(g):
      ans.append(k)
    p = "".join(ans)
    return p

test = int(input())
for i in range(test):
    s = input()
    print(rev_str(s))
