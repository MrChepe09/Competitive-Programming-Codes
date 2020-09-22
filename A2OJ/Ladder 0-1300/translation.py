def translation(a, b):
    return "YES" if a==b[::-1] else "NO"

a = input()
b = input()
print(translation(a, b))