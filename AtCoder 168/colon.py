import math
def colon(a, b, h, m):
  hour = 0.5 * (h * 60 + m) 
  minute = 6 * m
  angle = abs(hour - minute)
  angle = min(360 - angle, angle)
  rad = angle*(3.141592653589793238/180)
  #print(angle, rad)
  ans = math.sqrt(a**2+b**2-(2*a*b*(math.cos(rad))))
  return ans
  

a, b, h, m = map(int, input().split())
print(colon(a,b,h, m))
