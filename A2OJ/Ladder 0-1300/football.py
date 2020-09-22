def football(d):
    maxi = -1
    ans = 0
    for i in d:
        if(d[i]>maxi):
            ans = i
            maxi = d[i]
    return ans
            

n = int(input())
d = {}
for i in range(n):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

print(football(d))