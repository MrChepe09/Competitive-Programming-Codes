def team(n, a):
    count = 0
    for i in a:
        if(i.count(1)>=2):
            count+=1
    return count


n = int(input())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
print(team(n, arr))