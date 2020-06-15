def ttuple(ini, tar):
  diff = [0]*3
  for i in range(3):
    diff[i] = ini[i]-tar[i]
  c = diff.count(0)
  #0 Case
  if(diff[0] == 0 and diff[1] == 0 and diff[2] == 0):
    return 0

  #1 Case
  if((diff[0] == 0 and diff[1] == 0 and diff[2] != 0) or
       (diff[0] == 0 and diff[1] != 0 and diff[2] == 0) or
       (diff[0] != 0 and diff[1] == 0 and diff[2] == 0)):
    return 1
  if(diff[0]==diff[1] and diff[1]==diff[2]):
    return 1

  #2 Case
  #(+, +)
  if((diff[0]==diff[1] and diff[1]!=diff[2]) or
       (diff[0]==diff[2] and diff[1]!=diff[2]) or
       (diff[1]==diff[2] and diff[0]!=diff[2])):
    return 2
  if((diff[0]==0 and diff[1]!=diff[2]) or
     (diff[1]==0 and diff[0]!=diff[2]) or
     (diff[2]==0 and diff[1]!=diff[0])):
    return 2

  #(+, *)

  #(*, +)

  #(*, *)








  #3 Case
  return 3
    
  


test = int(input())
for i in range(test):
  t1 = list(map(int, input().split()))
  t2 = list(map(int, input().split()))
  print(ttuple(t1, t2))
