def hq9(s):
    if('H' in s or 'Q' in s or '9' in s):
        return "YES"
    return "NO"

s = input()
print(hq9(s))