def sheepwolve(s, w):
  if(w>=s):
    return "unsafe"
  else:
    return "safe"


s, w = map(int, input().split())
print(sheepwolve(s, w))
