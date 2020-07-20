def bitscore(s):
    l = list(s)
    score = int(max(s))*11 + int(min(s))*7
    if score >= 100:
        return str(score)[1:]
    return str(score)

def pairs(a):
    count = 0
    t = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if(((i+1)%2==0) and ((j+1)%2==0) and (t.count(a[i][0])<2) and (a[i][0] == a[j][0])):
                count += 1
                t.append(a[i][0])
            elif(((i+1)%2==1) and ((j+1)%2==1) and (t.count(a[i][0])<2) and (a[i][0] == a[j][0])):
                count += 1
                t.append(a[i][0])
    return count

n = int(input())
a = []
s = list(input().split())
for i in s:
    a.append(bitscore(i))
#print(a)
print(pairs(a))
