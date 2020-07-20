def bojack(d):
    res = 'a'*d
    res += 'b'*d
    return res


test = int(input())
for i in range(test):
    d = int(input())
    n = bojack(d)
    print(len(n))
    print(n)
