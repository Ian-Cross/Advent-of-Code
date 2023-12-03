
def to_base(num,b):
  """ takes in a integer number in base to and converts it to the specified base returns as a string """
  
  base_keys = { 0: '0', 1: '1', 2: '2', 3: '3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H' }

  ans = []
  while num > 0:
      ans.append(base_keys[num % b])
      num = int(num / b)
  
  return ''.join(str(_) for _ in ans[::-1])