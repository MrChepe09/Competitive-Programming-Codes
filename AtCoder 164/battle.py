import math
def monsterbattle(th, ts, ahh, ahs):
  tscore = math.ceil(ahh/ts)
  ascore = math.ceil(th/ahs)
  if(tscore<=ascore):
    return "Yes"
  else:
    return "No"

a, b, c, d = map(int, input().split())
print(monsterbattle(a, b, c, d))
