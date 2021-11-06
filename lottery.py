def lottery(a, b, c):
    if(a==7 or b==7 or c==7):
        return "YES"
    else:
        return "NO"
test = int(input())
for i in range(test):
    a, b, c = map(int, input().split())
    print(lottery(a, b, c))
