n = int(input())
c = list(map(int, input().rstrip().split()))
i = 0
jump = 0
while(i<n-1):
  if(i==n-2):
    i += 1
    jump += 1
  elif(c[i+2] == 0):
    i = i + 2
    jump += 1
  else:
    i = i + 1
    jump += 1
print(jump)
