def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(n - 1):
        previous, current = (current)%10, (previous + current)%10

    return current

test = int(input())
for i in range(test):
  n = int(input())
  print(get_fibonacci_last_digit_naive(n))
