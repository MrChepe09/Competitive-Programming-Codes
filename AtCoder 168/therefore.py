def therefore(n):
  a = [2, 4, 5, 7, 9]
  b = [0, 1, 6, 8]
  c = [3]
  z = int(str(n)[-1])
  if(z in a):
    return "hon"
  elif(z in b):
    return "pon"
  else:
    return "bon"

n = int(input())
print(therefore(n))
