from reused import arguments, read_file
from common.grid import Grid
from common.constants import CARDINAL_NEIGHBOURS
from common.tuples.addTuples import add_tup

PATH = "2024/day10/test.txt"

trailheads = []
seen = []
topi_map = None
count = 0

class trail_marker:
  value = -1
  pos = None
  parent = None
  children = []
  len_trail = -1

  def __init__(self,value,pos, parent = None, children = []):
    self.value = value
    self.pos = pos
    self.parent = parent
    self.children = children

def take_step(marker,p2 = False):
  global seen
  if topi_map.at(marker.pos).data == "9":
    if p2 or marker.pos not in seen:
      seen.append(marker.pos)
    return

  for neighbour in CARDINAL_NEIGHBOURS:
    new_pos = add_tup(marker.pos,neighbour)
    if not topi_map.in_bounds(new_pos):
      continue
    if int(topi_map.at(new_pos).data) - 1 == int(topi_map.at(marker.pos).data):
      new_marker = trail_marker(topi_map.at(new_pos).data,new_pos,marker,[])
      marker.children.append(new_marker)
      take_step(new_marker,p2)

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
    head = trail_marker(topi_map.at(trailhead).data, trailhead, None, [])    
    take_step(head)
    head.len_trail = len(seen)
    trails.append(head)
    seen = []

  return sum([trail.len_trail for trail in trails])


def part2(path):
  global trailheads, topi_map,seen
  file_data = read_file(path or PATH, return_type=str, strip=True)
  topi_map = Grid()
  topi_map.fill(file_data, callback=find_trailheads)

  trails = []
  for trailhead in trailheads:
    head = trail_marker(topi_map.at(trailhead).data, trailhead, None, [])    
    take_step(head, p2=True)
    head.len_trail = len(seen)
    trails.append(head)
    seen = []
    
  return sum([trail.len_trail for trail in trails])

if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")