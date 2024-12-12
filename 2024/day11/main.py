from reused import arguments, read_file
import sys

PATH = "2024/day11/test.txt"
sys.setrecursionlimit(10**6)

stone_library = {}
def stone_rules(val, blink):
  ''' How long is the list if val is evaluated blink times '''

  if (val,blink) in stone_library:
    return stone_library[(val,blink)]

  if blink == 0:
    ret = 1
  elif val == 0:
    ret = stone_rules(1, blink-1)
  elif len(str(val)) % 2 == 0:
    half = len(str(val)) // 2
    left,right = int(str(val)[:half]),int(str(val)[half:])
    ret = stone_rules(left, blink-1) + stone_rules(right, blink-1)
  else:
    ret = stone_rules(val*2024, blink-1)

  stone_library[(val,blink)] = ret
  return ret

def part1(path):
  file_data = read_file(path or PATH, return_type=int, strip=True, split=" ")
  return sum(stone_rules(x, 25) for x in file_data[0])

def part2(path):
  file_data = read_file(path or PATH, return_type=int, strip=True, split=" ")
  return sum(stone_rules(x, 75) for x in file_data[0])

if __name__ == "__main__":
  arguments(part1, part2)