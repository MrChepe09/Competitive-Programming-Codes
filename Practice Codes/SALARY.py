def salary(n, a):
    return sum(a)-(n*min(a))

test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    print(salary(n, a))