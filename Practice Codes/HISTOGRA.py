def histogram(n, a):
    sl = []
    sr = []
    


while(True):
    arr = list(map(int, input().split()))
    if(arr[0]==0):
        break
    n = arr[0]
    a = arr[1:]
    print(histogram(n, a))