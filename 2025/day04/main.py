from reused import arguments, read_file
from common.grid import Grid
from common.constants import NEIGHBOURS

PATH = "2025/day04/test.txt"

floor = Grid()
access_count = 0

def check_roll(row, row_num, col, col_num, replace = False):
  global access_count
  if col.data != '@':
    return
  
  n_count = 0
  for n in NEIGHBOURS:
    if floor.in_bounds((row_num,col_num),n):
      neighbour = floor.matrix[row_num + n[0]][col_num + n[1]]
      if neighbour.data == '@':
        n_count += 1
  if n_count < 4:
    if replace:
      col.data = 'x'
    access_count += 1

def part1(path):
  global floor, access_count
  file_data = read_file(path or PATH, return_type=str, strip=True)
  floor.fill(file_data)
  floor.traverse(check_roll)
  return access_count

def part2(path):
  global floor, access_count
  file_data = read_file(path or PATH, return_type=str, strip=True)
  floor.fill(file_data)

  pre_check = access_count - 1
  while pre_check != access_count:
    pre_check = access_count
    floor.traverse(lambda row, row_num, col, col_num: check_roll(row, row_num, col, col_num, replace=True))
  return access_count


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")