def IsGreaterOrEqual(digit, max_digit):
  return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))
  

def salary(n, a):
  ans = []
  while a!=[]:
    max_digit = 0
    for digit in a:
      if IsGreaterOrEqual(digit, max_digit):
        max_digit = digit
    ans.append(max_digit)
    a.remove(max_digit)
  return ans

n = int(input())
a = list(map(int, input().split()))
print(''.join([str(i) for i in salary(n, a)]))
