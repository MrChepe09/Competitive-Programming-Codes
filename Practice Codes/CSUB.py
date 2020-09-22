def substring(n, s):
    count = s.count('1')
    return ((count)*(count+1))//2

test = int(input())
for i in range(test):
    n = int(input())
    s = input()
    print(substring(n, s))