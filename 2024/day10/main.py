from reused import arguments, read_file
from common.grid import Grid
from common.constants import CARDINAL_NEIGHBOURS
from common.tuples.addTuples import add_tup

PATH = "2024/day10/test.txt"

trailheads = []
seen = []
topi_map = None

def take_step(marker,p2 = False):
  global seen
  if topi_map.at(marker).data == "9":
    if p2 or marker not in seen:
      seen.append(marker)
    return

  for neighbour in CARDINAL_NEIGHBOURS:
    new_pos = add_tup(marker, neighbour)
    if topi_map.in_bounds(new_pos) and int(topi_map.at(new_pos).data) - 1 == int(topi_map.at(marker).data):
      take_step(new_pos, p2)

def find_trailheads(row,row_num,col,col_num):
  global trailheads
  if col.data == "0":
    trailheads.append((row_num,col_num))

def part1(path):
  global trailheads, topi_map,seen
  file_data = read_file(path or PATH, return_type=str, strip=True)
  topi_map = Grid()
  topi_map.fill(file_data, callback=find_trailheads)

  trails = []
  for trailhead in trailheads:
    take_step(trailhead)
    trails.append(len(seen))
    seen = []

  return sum(trails)


def part2(path):
  global trailheads, topi_map,seen
  file_data = read_file(path or PATH, return_type=str, strip=True)
  topi_map = Grid()
  topi_map.fill(file_data, callback=find_trailheads)

  trails = []
  for trailhead in trailheads:
    take_step(trailhead, p2=True)
    trails.append(len(seen))
    seen = []
    
  return sum(trails)

if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")