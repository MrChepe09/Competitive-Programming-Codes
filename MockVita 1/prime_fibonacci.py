from itertools import permutations
def prime(n):
  for i in range(2, int(n**0.5)+1):
    if (n % i) == 0:
      return False
  return True

def fab(mi, ma, c):
  #print(mi, ma, c)
  for i in range(c-2):
    mi, ma = ma, mi+ma
  return ma
  
  
def primefab(n1, n2):
  primes = []
  final = []
  for i in range(n1, n2+1):
    if(prime(i)):
      primes.append(i)
  if(len(primes)==0):
    return 0
  if(len(primes)==1):
    return primes[0]
  perm = permutations(primes, 2)
  for i in perm:
    dig = str(i[0])+str(i[1])
    if(prime(int(dig))):
      final.append(int(dig))
  mini = min(final)
  maxi = max(final)
  return fab(mini, maxi, len(list(set(final))))
      


n1, n2 = map(int, input().split())
print(primefab(n1, n2))
