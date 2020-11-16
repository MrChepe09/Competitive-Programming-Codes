def floor(t, x):
    if t == 1 or t==2:
        return 1
    start = 2
    floor = 1
    while(t>start):
        floor += 1
        start += x
    return floor

test = int(input())
for i in range(test):
    t, x = map(int, input().split())
    print(floor(t, x))