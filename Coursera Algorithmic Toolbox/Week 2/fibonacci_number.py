def calc_fib(n):
    fib = [0]*(n+1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]        

test = int(input())
for i in range(test):
  n = int(input())
  print(calc_fib(n))
    
