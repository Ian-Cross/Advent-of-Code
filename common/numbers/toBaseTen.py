
def to_base_10(num: str, b: int):
  """ Takes in a string of a number in the specified base and converts it to a base 10 number """

  base_keys = {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6,'7':7,'8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17}

  k = 1
  ans = 0
  for c in num[::-1]:
    ans += base_keys[c] * k
    k = k * b
  return int(ans)


