test_cases = int(input())
for i in range(test_cases):
  children = [int(i) for i in input().split()]
  age = children[0]
  mid = 3
  eidi = children[mid]
  result = 0
  for j in range(1, mid):
    if(children[2] == children[0] and children[5] != children[3]):
      print("NOT FAIR")
      break
    elif(children[j] > age and children[mid+j] > eidi):
      result += 1
      age = children[j]
      eidi = children[mid+j]
    elif(children[j] < age and children[mid+j] < eidi):
      result += 1
      age = children[j]
      eidi = children[mid+j]
    elif(children[j] == age and children[mid+j] == eidi ):
      result += 1
      age = children[j]
      eidi = children[mid+j]
    else:
      print("NOT FAIR")
      break
  if(result == 2):
    print("FAIR")


    
