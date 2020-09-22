def cops(x, y, m, a):
    g = []
    check = y*m
    a.sort()
    for i in a:
        g.append([max(0, i-check), min(100, i+check)])
    ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    for i in g:
        #print(i[0], i[1])
        for j in range(i[0], i[1]+1):
            if(j in ans):
                ans.remove(j)
    return len(ans)
    


test = int(input())
for i in range(test):
    x, y, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(cops(x, y, m, a))