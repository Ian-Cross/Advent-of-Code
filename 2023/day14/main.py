from reused import arguments, read_file
from common.grid import Grid,Square
from collections import defaultdict

PATH = "2023/day14/test.txt"
grid = Grid()

def tilt():
  for col in range(grid.width):
    stop = (0,col)
    for row in range(grid.height):
      if grid.at((row,col)).data == 'O':
        if grid.in_bounds(stop):
          grid.set(stop,'O')

        if stop != (row,col):
          grid.set((row,col),'.')
        
        stop = (stop[0]+1,stop[1])
      elif grid.at((row,col)).data == '#':
        stop = (row+1,col)

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  grid.fill(file_data)
  
  tilt()

  total = 0
  for row in range(grid.height):
    for col in range(grid.width):
      if grid.at((row,col)).data == 'O':
        total += grid.height - row

  return total

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  grid.fill(file_data)
  sums = defaultdict(lambda: [])
  cycles = 1000000000
  for x in range(cycles):
  
    tilt()
    grid.rotate_90()
    tilt()
    grid.rotate_90()
    tilt()
    grid.rotate_90()
    tilt()
    grid.rotate_90()
    
    total = 0
    for row in range(grid.height):
      for col in range(grid.width):
        if grid.at((row,col)).data == 'O':
          total += grid.height - row
    sums[total].append(x)

    # print(x,total,sums[total]) This does not finish, analyize this to guestimate value at 1000000000
  print(total)


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")