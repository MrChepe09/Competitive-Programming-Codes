test_cases = int(input())
for i in range(test_cases):
  one = zero = 0
  seq = input()
  for j in range(len(seq)):
    if seq[j] == '1':
      one += 1
    else:
      zero += 1
  if(one%2==1):
    print("WIN")
  else:
    print("LOSE")
