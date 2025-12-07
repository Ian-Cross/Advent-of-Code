from reused import arguments, read_file
from common.grid import Grid
import operator
from math import prod

PATH = "2025/day06/test.txt"

def fill(row, row_num, col, col_num):
  if col.data.isnumeric():
    col.data = col.data.zfill(4)

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, split=" |\n", exclude_none=True)
  grid = Grid()
  grid.fill(file_data)

  grand_total = 0
  for i in range(grid.width):
    op = operator.mul if grid.at((grid.height-1,i)).data == "*" else operator.add
    total = 1 if op == operator.mul else 0
    for j in range(grid.height - 2,-1,-1):
      total = op(total,int(grid.at((j,i)).data))
    grand_total += total
  return grand_total

def part2(path):
  file_data = read_file(path or PATH, return_type=str, split="\n", as_one=True)
  file_data = file_data[:-1]

  grand_total = 0
  op,buffer = None, []
  for i in range(len(file_data[0])-1,-1,-1):
    op = prod if file_data[-1][i] == "*" else sum if file_data[-1][i] == "+" else None
    buffer.append("".join(file_data[l][i] for l in range(len(file_data)-2,-1,-1)).strip()[::-1])

    if not op:
      continue

    grand_total += op(int(b) for b in buffer if b.isnumeric())
    op,buffer = None, []

  return grand_total

if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")