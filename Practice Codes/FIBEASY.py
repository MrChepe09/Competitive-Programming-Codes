test_cases = int(input())
for i in range(test_cases):
  fabinteger = int(input())
  if(fabinteger == 1):
    print("0")
  else:
    series = [0]*fabinteger
    series[0] = 0
    series[1] = 1
    for j in range(2, fabinteger):
      series[j] = (series[j-1] + series[j-2])%10
    length = len(series)
    p = length%4
    print(series[length-p-1])
