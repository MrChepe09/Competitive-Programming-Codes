def position(n, a, b):
    return (n - max(a + 1, n - b) + 1)

n, a, b = map(int, input().split())
print(position(n, a, b))