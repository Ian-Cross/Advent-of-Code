from reused import arguments, read_file
from functools import reduce
import operator

PATH = "2023/day03/test.txt"

neighbours = [(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)]

def in_bounds(pos,n,k):
  if pos[1]+n[1] >= k or pos[1]+n[1] < 0:
    return False
  if pos[0]+n[0] >= k or pos[0]+n[0] < 0:
    return False
  return True

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
    
  k = len(file_data[0])
  grid = [['.']*k for _ in range(k)]
  symbols = []

  for y,line in enumerate(file_data):
    for x,c in enumerate(line):
      grid[y][x] = c
      if not c.isnumeric() and c != ".":
        symbols.append((y,x))
  
  sum = 0
  for s in symbols:
    for n in neighbours:
      if not in_bounds(s,n,k):
        continue

      (y,x) = (s[0]+n[0],s[1]+n[1])
      num = grid[y][x]

      if not num.isnumeric():
        continue

      grid[y][x] = '.'

      p = x-1
      while p >= 0 and grid[y][p].isnumeric():
        num = grid[y][p] + num
        grid[y][p] = '.'
        p-=1

      p = x+1
      while p < k and grid[y][p].isnumeric():
        num += grid[y][p]
        grid[y][p] = '.'
        p+=1
      
      sum += int(num)
  return sum

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)

  k = len(file_data[0])
  grid = [['.']*k for _ in range(k)]
  gears = set()

  for y,line in enumerate(file_data):
    for x,c in enumerate(line):
      grid[y][x] = c
      if c == "*":
        gears.add((y,x))
  
  ratios = 0
  for gear in gears:
    nums = []
    for n in neighbours:
      if not in_bounds(gear,n,k):
        continue

      y,x = gear[0]+n[0],gear[1]+n[1]
      num = grid[y][x]

      if num.isnumeric():
        grid[y][x] = '.'
        p = x - 1
        while p >= 0 and grid[y][p].isnumeric():
          num = grid[y][p] + num
          grid[y][p] = '.'
          p-=1

        p = x+1
        while p < k and grid[y][p].isnumeric():
          num += grid[y][p]
          grid[y][p] = '.'
          p+=1

        nums.append(int(num))
    if len(nums) > 1:
      ratios += reduce(operator.mul,nums,1)

  return ratios


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")