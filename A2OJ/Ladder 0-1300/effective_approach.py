from bisect import bisect_left
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1

def approach(n, ans):
    global a
    g = BinarySearch(a, n)
    ans[0] += g+1
    ans[1] += len(a)-g
    return ans


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ans = [0, 0]
for i in b:
    ans = approach(i, ans)
print(*ans)