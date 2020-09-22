def elephants(n, c, a):
    if(sum(a)<=c):
        return "Yes"
    else:
        return "No"
        
test = int(input())
for i in range(test):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    print(elephants(n, c, a))