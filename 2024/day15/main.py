from reused import arguments, read_file
from common.grid import Grid
from common.constants import NEIGHBOURS_MAP
from common.tuples.addTuples import add_tup
from collections import defaultdict
from copy import deepcopy
from tqdm import tqdm

PATH = "2024/day15/test.txt"

warehouse = Grid()
robot_pos = (0,0)

key_map = {
  '^': NEIGHBOURS_MAP['u'],
  'v': NEIGHBOURS_MAP['d'],
  '<': NEIGHBOURS_MAP['l'],
  '>': NEIGHBOURS_MAP['r'],
}

def find_robot(row,row_num,col,col_num):
  global robot_pos
  if col.data == "@":
    robot_pos = (row_num,col_num)
  
def expand(warehouse_state):
  state = []
  for row in warehouse_state:
    new_row = ""
    for col in row:
      if col == '#':
        new_row += '##'
      elif col == '.':
        new_row += '..'
      elif col == '@':
        new_row += '@.'
      elif col == 'O':
        new_row += '[]'
    state.append(new_row)
  return state

def part1(path):
  global warehouse, robot_pos
  file_data = read_file(path or PATH, return_type=str, strip=True, as_one=True)
  warehouse_state,directions = file_data.split("\n\n")
  warehouse.fill(warehouse_state.split("\n"),callback=find_robot)


  def check_ahead(pos,direction):
    global warehouse
    nodes = []
    next_pos = pos
    while True:
      next_pos = add_tup(next_pos,direction)
      if not warehouse.in_bounds(next_pos) or warehouse.at(next_pos).data == '#':
        return []
      if warehouse.at(next_pos).data == '.':
        nodes.append(next_pos)
        return nodes
      
      nodes.append(next_pos)


  for dir in directions:
    if dir not in key_map:
      continue
    
    next_pos = add_tup(robot_pos,key_map[dir])
    if not warehouse.in_bounds(next_pos) or warehouse.at(next_pos).data == '#':
      continue

    for node in check_ahead(robot_pos,key_map[dir])[::-1]:
      warehouse.at(node).data = 'O'
    
    warehouse.at(robot_pos).data = '.'
    robot_pos = node
    warehouse.at(robot_pos).data = '@'

  total = 0
  def gps_sum(row,row_num,col,col_num):
    nonlocal total
    if col.data == 'O':
      total += row_num*100 + col_num

  warehouse.traverse(gps_sum)
  return total

def part2(path):
  global warehouse, robot_pos
  file_data = read_file(path or PATH, return_type=str, strip=True, as_one=True)
  warehouse_state,directions = file_data.split("\n\n")
  warehouse_state = expand(warehouse_state.split("\n"))
  warehouse.fill(warehouse_state,callback=find_robot)

  def check_ahead_wide(pos,direction):
    global warehouse, robot_pos
    next_pos = add_tup(pos,direction)
    nodes = []
    if not warehouse.in_bounds(next_pos) or warehouse.at(next_pos).data == '#':
      return [-1]
    
    if warehouse.at(next_pos).data == '.':
      nodes = [next_pos]
    elif warehouse.at(next_pos).data == '[' and direction in [NEIGHBOURS_MAP['u'],NEIGHBOURS_MAP['d']]:
      nodes = [next_pos] + check_ahead_wide(next_pos, direction) + check_ahead_wide(add_tup(next_pos,NEIGHBOURS_MAP['r']), direction)
    elif warehouse.at(next_pos).data == '[':
      nodes = [next_pos] + check_ahead_wide(next_pos, direction)
    elif warehouse.at(next_pos).data == ']' and direction in [NEIGHBOURS_MAP['u'],NEIGHBOURS_MAP['d']]:
      nodes = [next_pos] + check_ahead_wide(add_tup(next_pos,NEIGHBOURS_MAP['l']), direction) + check_ahead_wide(next_pos, direction)
    elif warehouse.at(next_pos).data == ']':
      nodes = [next_pos] + check_ahead_wide(next_pos, direction)

    return nodes


  for dir in tqdm(directions):
    if dir not in key_map:
      continue
    
    next_pos = add_tup(robot_pos,key_map[dir])
    if not warehouse.in_bounds(next_pos) or warehouse.at(next_pos).data == '#':
      continue

    nodes = check_ahead_wide(robot_pos,key_map[dir])
    if not nodes or -1 in nodes:
      continue

    warehouse_copy = deepcopy(warehouse)
    if dir == '^':
      columns = defaultdict(set)
      for node in nodes[::-1]:
        columns[node[1]].add(node)
        warehouse.at((node[0]+1,node[1])).data = '.'

      for col in columns.values():
        for node in sorted(list(col),key=lambda x: x[0]):
          warehouse.at(node).data = warehouse_copy.at((node[0]+1,node[1])).data

      lowest = (0,0)
      for node in nodes:
        if node[0] > lowest[0]:
          lowest = node

      warehouse.at(robot_pos).data = '.'
      robot_pos = lowest
      warehouse.at(robot_pos).data = '@'

    elif dir == 'v':
      columns = defaultdict(set)
      for node in nodes[::-1]:
        columns[node[1]].add(node)
        warehouse.at((node[0]-1,node[1])).data = '.'

    
      for col in columns.values():
        for node in sorted(list(col),key=lambda x: x[0], reverse=True):
          warehouse.at(node).data = warehouse_copy.at((node[0]-1,node[1])).data

      highest = (10**6,0)
      for node in nodes:
        if node[0] < highest[0]:
          highest = node
      
      warehouse.at(robot_pos).data = '.'
      robot_pos = highest
      warehouse.at(robot_pos).data = '@'

    elif dir == '<' or dir == '>':
      for idx,node in enumerate(reversed(nodes[1:])):
        next_node = len(nodes)-idx-2
        warehouse.at(node).data = warehouse.at(nodes[next_node]).data

      warehouse.at(robot_pos).data = '.'
      robot_pos = nodes[0]
      warehouse.at(robot_pos).data = '@'

  total = 0
  def gps_sum(row,row_num,col,col_num):
    nonlocal total
    if col.data == '[':
      total += row_num*100 + col_num

  warehouse.traverse(gps_sum)
  return total


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")