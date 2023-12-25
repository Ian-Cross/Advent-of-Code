from reused import arguments, read_file
from functools import cmp_to_key
from collections import defaultdict
from copy import deepcopy

PATH = "2023/day22/test.txt"
grid = None
grid_sizes = (0,0,0)
x,y,z = 0,1,2
s,e = 0,1

def build_bricks(data):
  global grid_sizes
  bricks = []
  for i,line in enumerate(data):
    start,end = line.split("~")
    start = tuple([int(_) for _ in start.split(",")])
    end = tuple([int(_) for _ in end.split(",")])
    grid_sizes = tuple(map(max,zip(grid_sizes,tuple(map(max,zip(start,end))))))

    bricks.append((start,end,[],i))
  return bricks

def build_grid():
  grid = [] 
  for z_row in range(grid_sizes[z]+1):
    matrix = []
    for y_row in range(grid_sizes[y]+1):
      row = ['.']*(grid_sizes[x]+1)
      matrix.append(row)
    grid.append(matrix)
  return grid

def simulate_gravity(bricks):
  for brick in bricks:
    brick = extend_brick(brick)

    while True:
      flag = False
      for cube in brick[2]:
        if cube[z] == 0:
          flag = True
          break

        if grid[cube[z]-1][cube[y]][cube[x]] != '.':
          flag = True
          break

      if flag:
        for z_i,z_row in enumerate(grid):
          for y_i,y_row in enumerate(z_row):
            for x_i,_ in enumerate(y_row):
              if (x_i,y_i,z_i) in brick[2]:
                grid[z_i][y_i][x_i] = brick[3]
        break

      # Lower:
      for c_i,cube in enumerate(brick[2]):
        brick[2][c_i] = (cube[x],cube[y],cube[z]-1)
  return bricks

def check_supports(bricks):
  supports = []
  occurances = defaultdict(lambda: 0)
  removeable = []
  for brick in bricks:
    top_row = brick[2][-1][z]
    next_row = top_row+1
    ids = set()

    for cube in brick[2]:
      if grid[next_row][cube[y]][cube[x]] != '.':
        ids.add(grid[next_row][cube[y]][cube[x]])
    if len(ids):
      for id in ids:
        occurances[id] += 1
      supports.append((brick[3],ids))
    else:
      removeable.append(brick[3])
  return supports,occurances,removeable

def extend_brick(brick):
  if (brick[s][x] != brick[e][x]):
    for _ in range(brick[s][x],brick[e][x]+1):
      brick[2].append((_,brick[s][y],brick[s][z]))    
  elif (brick[s][y] != brick[e][y]):
    for _ in range(brick[s][y],brick[e][y]+1):
      brick[2].append((brick[s][x],_,brick[s][z]))
  elif (brick[s][z] != brick[e][z]):
    for _ in range(brick[s][z],brick[e][z]+1):
      brick[2].append((brick[s][x],brick[s][y],_))
  else:
    brick[2].append(brick[s])
  return brick


def sort_by_z(a,b):
  if a[s][z] > b[s][z]:
    return 1
  if a[s][z] == b[s][z]:
    return 0
  if a[s][z] < b[s][z]:
    return -1

def part1(path):
  global grid
  file_data = read_file(path or PATH, return_type=str, strip=True)

  bricks = build_bricks(file_data)

  sort_by_z_key = cmp_to_key(sort_by_z)
  bricks.sort(key=sort_by_z_key)
  
  grid = build_grid()
  
  bricks = simulate_gravity(bricks)

  supports,occurances,removeable = check_supports(bricks)

  for id,support in supports:
    flag = True
    for s in support:
      if occurances[s] == 1:
        flag = False
        break
    if flag:
      removeable.append(id)
  return len(removeable)


def part2(path):
  global grid
  file_data = read_file(path or PATH, return_type=str, strip=True)

  bricks = build_bricks(file_data)

  sort_by_z_key = cmp_to_key(sort_by_z)
  bricks.sort(key=sort_by_z_key)
  
  grid = build_grid()
  
  bricks = simulate_gravity(bricks)

  supports,occurances,_ = check_supports(bricks)

  total = 0
  for i,support in supports:
    queue = [s for s in support]
    count_copy = deepcopy(occurances)
    while queue:
      q = queue.pop(0)
      count_copy[q] -= 1
      if count_copy[q] == 0:
        for id,s in supports:
          if q == id:
            queue += list(s)
            break
    for c in count_copy:
      if count_copy[c] == 0:
        total += 1
  return total


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")