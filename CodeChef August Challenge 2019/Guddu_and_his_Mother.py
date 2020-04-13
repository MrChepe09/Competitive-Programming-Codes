test_cases = int(input())
for n in range(test_cases):
  number = int(input())
  output = 0
  sequence = [int(i) for i in input().split()]
  for i in range(number):
    xor = sequence[i]
    for j in range(i+1, number):
      xor = xor^sequence[j]
      if xor in sequence:
        k = sequence.index(xor)
        if k>j and j>i:
          output += 2
  print(output)
    
