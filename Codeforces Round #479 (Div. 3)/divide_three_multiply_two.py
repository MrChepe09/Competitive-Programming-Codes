def problemD(n, a):
    three = []
    two = []
    both = []
    ans = []
    for i in a:
        if(i%3==0 and i%2==1):
            three.append(i)
        elif(i%3!=0 and i%2==0):
            two.append(i)
        elif(i%3==0 and i%2==0):
            both.append(i)
    three.sort(reverse=True)
    two.sort()
    both.sort(reverse=True)
    ans.append(three[0])
    for i in range(1, len(three)):
        if(three[i]*3 == ans[-1]):
    
    


n = int(input())
a = list(map(int, input().split()))
print(problemD(n, a))
