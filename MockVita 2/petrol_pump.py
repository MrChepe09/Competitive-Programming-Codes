def petrol(a):
    sum = 0
    n = 0
    for i in range(len(a)):
        n+=1
        sum+=a[i]
    mini = miniu(a, n, 0, sum)
    sum -= mini
    sum /= 2
    return sum+mini

def miniu(arr, n, sum1, sum2):
    if(n==0):
        return abs((sum2-sum1)-sum1)
    return min(miniu(arr, n-1, sum1+arr[n-1], sum2), miniu(arr, n-1, sum1, sum2))

a = list(map(int, input().split()))
print(int(petrol(a)))
