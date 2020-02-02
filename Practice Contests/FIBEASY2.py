finallist = [3, 0, 7, 9, 6, 3, 5]
test_cases = int(input())
for i in range(test_cases):
  fabinteger = int(input())
  fabinteger = fabinteger%60
  p = int(fabinteger/8)
  if(fabinteger == 1 or fabinteger==0):
    print("0")
  elif(fabinteger<4 and fabinteger>1):
    print("1")
  elif(fabinteger>=4 and fabinteger<8):
    print("2")
  else:
    print(finallist[p-1])
