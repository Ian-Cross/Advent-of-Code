from math import gcd

def lcm (arr):
  x = 1
  for i in arr:
      x = x*i//gcd(x, i)
  return x