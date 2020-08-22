def maths(s):
    arr = []
    for i in range(0, len(s), 2):
        arr.append(int(s[i]))
    arr.sort()
    ans = ''
    for i in arr:
        ans = ans + str(i)+'+'
    return ans[:len(s)]

s = input()
print(maths(s))