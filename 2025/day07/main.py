from reused import arguments, read_file
from common.grid import Grid

PATH = "2025/day07/test.txt"

grid = Grid()
split_count = 0

def convert(_,__,col,___):
  if col.data == ".":
    col.data = 0
  if col.data == "S":
    col.data = 1

def track_particles(_,row_num,col,col_num):
  global grid, split_count

  if row_num == 0:
    return

  above = grid.get((row_num-1,col_num))
  if above == 0 or above == "^":
    return

  if col.data == "^":
    split_count += 1
    grid.set((row_num,col_num-1), grid.get((row_num,col_num-1)) + above)
    grid.set((row_num,col_num+1), grid.get((row_num,col_num+1)) + above)
  else:
    col.data += above

def process(data):
  global grid
  grid.fill(data)
  grid.traverse(convert)
  grid.traverse(track_particles)

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  process(file_data)
  return split_count

def part2(path):
  global grid
  file_data = read_file(path or PATH, return_type=str, strip=True)
  process(file_data)
  return sum([col.data for col in grid.row(-1)])

if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")