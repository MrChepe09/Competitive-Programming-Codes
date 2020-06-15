import sys

def optimal_sequence(n):
    if n == 1:
        return [1]
    ans = primcalc(n)
    return construct_min_list(n, ans)

def construct_min_list(n, ops):
    sequence = []
    while n > 0:
        sequence.append(n)
        if n % 2 != 0 and n % 3 != 0:
            n = n - 1
        elif n % 2 == 0 and n % 3 == 0: 
            n = n // 3
        elif n % 2 == 0:
            if ops[n-1] < ops[n//2]:
                n = n-1
            else:
                n = n // 2
        elif n % 3 == 0: 
            if ops[n-1] < ops[n//3]:
                n = n-1
            else:
                n = n // 3
    return reversed(sequence)
  
def primcalc(n):
  result = [0 for _ in range(n+1)]
  for i in range(2, n+1):
    m1 = result[i-1]
    m2 = sys.maxsize
    m3 = sys.maxsize
    if(i%2==0):
      m2 = result[int(n/2)]
    if(i%3==0):
      m3 = result[int(n/3)]

    mini = min(m1, m2, m3)
    result[i] = mini+1
  return result


n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence)-1)
print(*sequence)
#print(*b)
