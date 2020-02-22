from collections import deque
stack = deque()
test = int(input())
for i in range(test):
  count = 0
  n = int(input())
  l = list(map(int, input().split()))
  stack.append(l[n-1])
  l.pop()
  for j in range(n-2, -1, -1):
    stack.append(l[j])
    l.pop()
    count += 1
    if(stack[count]<stack[count-1]):
      stack[count], stack[count-1] = stack[count-1], stack[count]
      break
  if(count==0):
    print(-1)
  else:
    print("".join(map(str, l)))
    
    
