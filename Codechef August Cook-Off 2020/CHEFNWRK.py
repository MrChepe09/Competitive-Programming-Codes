def boxes(n, k, a):
    count = 1
    hand = 0
    for i in range(n):
        if(a[i]>k):
            return -1
        if(hand+a[i]>k):
            hand = a[i]
            count += 1
            continue
        hand+=a[i]
    return count

test = int(input())
for i in range(test):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(boxes(n, k, a))
