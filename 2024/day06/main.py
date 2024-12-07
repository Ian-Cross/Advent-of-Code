from reused import arguments, read_file
from common.grid import Grid
from common.constants import NEIGHBOURS_MAP
from common.tuples.addTuples import add_tup

PATH = "2024/day06/test.txt"

floor = Grid()
guard_start = (0,0)

def find_guard(row,row_num,col,col_num):
  global guard_start
  if col.data == "^":
    guard_start = (row_num,col_num)
    return True
  return False

def part1(path):
  global floor, guard_start

  path = PATH
  
  file_data = read_file(path or PATH, return_type=str, strip=True)
  floor.fill(file_data, callback=find_guard)  
  directions = ['n','e','s','w']
  facing = 0

  visited = set()
  
  guard_pos = guard_start  
  while floor.in_bounds(guard_pos, NEIGHBOURS_MAP[directions[facing]]):
    next_pos = add_tup(guard_pos, NEIGHBOURS_MAP[directions[facing]])
    if floor.at(next_pos).data == "#":
      facing = (facing + 1) % 4
      continue
    
    visited.add(next_pos)
    guard_pos = next_pos
  
  return len(visited)

def part2(path):
  global floor
  path = PATH

  file_data = read_file(path or PATH, return_type=str, strip=True)
  floor.fill(file_data, callback=find_guard)
  loops = 0

  def guard_walk(row,row_num,col,col_num):
    global guard_start
    nonlocal loops
    directions = ['n','e','s','w']
    facing = 0
    route = set()
    guard_pos = guard_start

    while True:
      if (guard_pos[0],guard_pos[1],facing) in route:
        loops += 1
        break
      
      route.add((guard_pos[0],guard_pos[1],facing))

      next_pos = add_tup(guard_pos, NEIGHBOURS_MAP[directions[facing]])
      if not floor.in_bounds(next_pos):
        break
      
      if floor.at(next_pos).data == "#" or next_pos == (row_num,col_num):
        facing = (facing + 1) % 4
      else:
        guard_pos = next_pos


  floor.traverse(guard_walk)

  return loops

if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")