def minions(n, k, a):
    count = 0
    for i in a:
        if((i+k)%7==0):
            count+=1
    return count


test = int(input())
for i in range(test):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(minions(n, k, a))