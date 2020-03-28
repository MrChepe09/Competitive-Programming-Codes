def swap_sum(a, b):
  la = list(a)
  lb = list(b)
  if(len(la)==1 and len(lb)==1):
    return (strl(la, lb))
  elif(len(la)==1):
    for j in range(len(lb)):
      if(int(a)>int(lb[j])):
        la[0], lb[j] = lb[j], la[0]
        break
    return (strl(la, lb))
  elif(len(lb)==1):
    for j in range(len(la)):
      if(int(b)>int(la[j])):
        lb[0], la[j] = la[j], lb[0]
        break
    return (strl(la, lb))
  else:
    mins = min(int(a), int(b))
    if(mins == int(a)):
      if(la[0]<lb[1]):
        la[0], lb[1] = lb[1], la[0]
    else:
      if(lb[0]<la[1]):
        lb[0], la[1] = la[1], lb[0]
    return(strl(la, lb))  

def strl(la, lb):
  lastr = ''.join([str(elem) for elem in la])
  lbstr = ''.join([str(elem) for elem in lb])
  return (int(lastr)+int(lbstr))

test = int(input())
for i in range(test):
  a, b = input().split()
  print(swap_sum(a, b))
