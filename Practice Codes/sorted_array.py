def sort_arr(n, a):
    a.sort()
    return a

test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    g = (sort_arr(n, a))
    print(*g)
