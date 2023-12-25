from reused import arguments, read_file
from common.grid import Grid, Square


PATH = "2023/day11/test.txt"
grid = Grid()
galaxies = []

def find_galaxies(row,row_num,col,col_num):
  global galaxies
  if col.data == '#':
    galaxies.append((row_num,col_num))

def part1(path):
  global galaxies
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  grid.fill(file_data)

  empty_rows = []
  offset = 0
  for row_num,row in enumerate(grid.matrix):
    if all([ x.data == '.' for x in row]):
      empty_rows.append(row_num + offset)
      offset += 1

  for row_num in empty_rows:
    grid.insert_row([Square('.')]*grid.width,row_num)

  empty_cols = []
  offset = 0
  for col_num in range(grid.width):
    if all([x.data == '.' for x in [grid.matrix[r][col_num] for r in range(grid.height)]]):
      empty_cols.append(col_num + offset)
      offset += 1

  for col_num in empty_cols:
    grid.insert_column([Square('.')]*grid.height,col_num)
  
  grid.traverse(find_galaxies)

  total_distance = 0
  for i in range(len(galaxies)):
    for j in range(i+1,len(galaxies)):
      total_distance += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

  return total_distance

def part2(path):
  global galaxies
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  grid.fill(file_data)

  empty_rows = []
  for row_num,row in enumerate(grid.matrix):
    if all([ x.data == '.' for x in row]):
      empty_rows.append(row_num)

  empty_cols = []
  for col_num in range(grid.width):
    if all([x.data == '.' for x in [grid.matrix[r][col_num] for r in range(grid.height)]]):
      empty_cols.append(col_num)
  
  grid.traverse(find_galaxies)

  total_distance = 0
  MUL = 999999
  for i in range(len(galaxies)):
    for j in range(i+1,len(galaxies)):

      r1,r2 = max(galaxies[i][0],galaxies[j][0]),min(galaxies[i][0],galaxies[j][0])
      c1,c2 = max(galaxies[i][1],galaxies[j][1]),min(galaxies[i][1],galaxies[j][1])

      stradle_r = [x for x in empty_rows if r2 < x < r1]
      stradle_c = [x for x in empty_cols if c2 < x < c1]

      total_distance += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]) + len(stradle_c)*MUL + len(stradle_r)*MUL

  return total_distance


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")