n = int(input())
done = [0]
count = 0
leftChild = list(map(int, input().split()))
rightChild = list(map(int, input().split()))
for i in range(n):
  if(leftChild[i] == -1 and rightChild[i] == -1):
    count+=1
  elif(leftChild[i] == -1 and rightChild[i] != -1):
    if (rightChild[i] not in done):
      if(leftChild[i-1] == -1 and rightChild[i-1] == -1 and leftChild[i-2] == -1 and rightChild[i-2] == -1):
        break
      else:
        done.append(rightChild[i])
        count+=1
    else:
      break
  elif(leftChild[i] != -1 and rightChild[i] == -1):
    if (leftChild[i] not in done):
      if(leftChild[i-1] == -1 and rightChild[i-1] == -1 and leftChild[i-2] == -1 and rightChild[i-2] == -1):
        break
      else:
        done.append(leftChild[i])
        count+=1
    else:
      break
  elif(leftChild[i] != -1 and rightChild[i] != -1):
    if (leftChild[i] not in done and rightChild[i] not in done):
      if(leftChild[i-1] == -1 and rightChild[i-1] == -1 and leftChild[i-2] == -1 and rightChild[i-2] == -1):
        break
      else:
        done.append(leftChild[i])
        done.append(rightChild[i])
        count+=1
    else:
      break
if(count==n):
  print('true')
else:
  print('false')
