from reused import arguments, read_file
from common.grid import Grid

PATH = "2023/day13/test.txt"

def check_hor_mirror(i,j,grid, num_smudges):
  smudges = 0
  while i >= 0 and j < grid.height:
    for x in range(grid.width):
      if grid.at((i,x)) != grid.at((j,x)):
        smudges += 1
    i-=1
    j+=1
  return smudges == num_smudges


def check_vert_mirror(i,j,grid, num_smudges):
  smudges = 0
  while i >= 0 and j < grid.width:
    for y in range(grid.height):
      if grid.at((y,i)) != grid.at((y,j)):
        smudges += 1
    i-=1
    j+=1
  return smudges == num_smudges


def find_reflection(grid, num_smudges = 0):
  reflection = -1
  for y in range(grid.height-1):
    if check_hor_mirror(y,y+1,grid, num_smudges):
      reflection = y+1

  if reflection != -1:
    return reflection*100

  reflection = -1
  for x in range(grid.width-1):
    for y in range(grid.height):
      if check_vert_mirror(x,x+1,grid,num_smudges):
        reflection = x+1
  if reflection != -1:
    return reflection

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, as_one=True,split="\n\n")
  
  sum = 0
  for pattern in file_data:
    grid = Grid()
    grid.fill(pattern.split("\n"))
    sum += find_reflection(grid)
  return sum



def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, as_one=True,split="\n\n")
  
  sum = 0
  for pattern in file_data:
    grid = Grid()
    grid.fill(pattern.split("\n"))
    sum += find_reflection(grid,num_smudges = 1)
  return sum


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")