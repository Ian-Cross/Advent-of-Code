from reused import arguments, read_file
from common.grid import Grid
from common.constants import NEIGHBOURS, ORDINAL_NEIGHBOURS
from common.tuples.addTuples import add_tup

PATH = "2024/day04/input.txt"

def part1(path):
  path = PATH
  file_data = read_file(path or PATH, return_type=str, strip=True)
  word_grid = Grid()
  word_grid.fill(file_data)

  word_count = 0

  def count_words(row,row_num,col,col_num):
    nonlocal word_count
    if col.data != 'X':
      return
    
    search = ["M","A","S"]
    for neighbour in NEIGHBOURS:
      neighbour_pos = (row_num, col_num)
      match = True
      for char in search:
        neighbour_pos = add_tup(neighbour_pos, neighbour)
        if not word_grid.in_bounds(neighbour_pos) or word_grid.at(neighbour_pos).data != char:
          match = False
          break
      if match:
        word_count += 1

  word_grid.traverse(count_words)

  return word_count

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  word_grid = Grid()
  word_grid.fill(file_data)

  word_count = 0

  def count_words(row,row_num,col,col_num):
    nonlocal word_count
    
    if col.data != 'A':
      return

    search_pattern = [(ORDINAL_NEIGHBOURS[0],ORDINAL_NEIGHBOURS[3]),(ORDINAL_NEIGHBOURS[1],ORDINAL_NEIGHBOURS[2])]
    for search in search_pattern:
      neighbour_pos = add_tup((row_num, col_num), search[0])
      if not word_grid.in_bounds(neighbour_pos):
        return
      
      first_neighbour = word_grid.at(neighbour_pos)
      if first_neighbour.data != 'M' and first_neighbour.data != 'S':
        return

      neighbour_pos = add_tup((row_num, col_num), search[1])
      if not word_grid.in_bounds(neighbour_pos):
        return
      
      combo = (first_neighbour.data,word_grid.at(neighbour_pos).data)
      if combo != ('M','S') and combo != ('S','M'):
        return
    word_count += 1
  
  word_grid.traverse(count_words)
  return word_count

if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")