from reused import arguments, read_file
from common.grid import Grid, Square
from common.constants import CARDINAL_NEIGHBOURS, NEIGHBOURS
from collections import defaultdict

PATH = "2023/day10/test.txt"

start = (0,0)
grid = Grid()
loop: list[tuple[int,int]] = []
pipe_map = {
  '|': [(-1,0),(1,0)],
  '-': [(0,1),(0,-1)],
  'L': [(-1,0),(0,1)],
  'J': [(-1,0),(0,-1)],
  '7': [(1,0),(0,-1)],
  'F': [(1,0),(0,1)],
  '.': [],
  'S': []
}

def interpret_start_pipe():
  global start, grid

  must_connect = []
  for neighbour in NEIGHBOURS:
    if not grid.in_bounds(start,neighbour):
      continue
    relative_neighbour = tuple(map(sum, zip(start, neighbour)))
    curr = grid.at(relative_neighbour)
    for direction in pipe_map[curr.data]:
      if tuple(map(sum, zip(direction,relative_neighbour))) == start:
        must_connect.append(direction)

  for pipe in pipe_map:
    if len(pipe_map[pipe]) == 0:
      continue
    if tuple(map(sum, zip(pipe_map[pipe][0],must_connect[0]))) == (0,0):
      if tuple(map(sum, zip(pipe_map[pipe][1],must_connect[1]))) == (0,0):
        grid.set(start,pipe)
        return
    if tuple(map(sum, zip(pipe_map[pipe][1],must_connect[0]))) == (0,0):
      if tuple(map(sum, zip(pipe_map[pipe][0],must_connect[1]))) == (0,0):
        grid.set(start,pipe)
        return


def count_steps(pos,steps):
  global grid,start,loop

  steps = 0
  last_pos = None

  while True:
    loop.append(pos)
    if pos == start and steps != 0:
      break
  
    directions = pipe_map[grid.at(pos).data]
  
    dir_1 = tuple( map( sum, zip(pos,directions[0]) ) )
    dir_2 = tuple( map( sum, zip(pos,directions[1]) ) )

    if last_pos == None:
      last_pos = pos
      pos = dir_1
    elif dir_1 != last_pos:
      last_pos = pos
      pos = dir_1
    else:
      last_pos = pos
      pos = dir_2

    steps += 1

  return steps//2


def setStart(row,row_num,col,col_num):
  global start
  if col.data == 'S':
    start = (row_num,col_num)


def clear_trash(row,row_num,col,col_num):
  global loop,grid
  if (row_num,col_num) not in loop:
    grid.set((row_num,col_num),'.')


def scale_grid(grid,big_grid):
  big_grid.height = grid.height*3
  big_grid.width = grid.width*3

  big_grid.matrix = [[Square('.') for x in range(big_grid.width)] for y in range(big_grid.height)]

  scale = {
    '.': [
      [',',',',','],
      [',','.',','],
      [',',',',','],
    ],
    '|': [
      [',','|',','],
      [',','|',','],
      [',','|',','],
    ],
    '-': [
      [',',',',','],
      ['-','-','-'],
      [',',',',','],
    ],
    'L': [
      [',','|',','],
      [',','L','-'],
      [',',',',','],
    ],
    'J': [
      [',','|',','],
      ['-','J',','],
      [',',',',','],
    ],
    'F': [
      [',',',',','],
      [',','F','-'],
      [',','|',','],
    ],
    '7': [
      [',',',',','],
      ['-','7',','],
      [',','|',','],
    ],
  }

  for y in range(grid.height):
    for x in range(grid.width):
      by,bx = 1+y*3,1+x*3
      big_grid.set((by,bx),grid.at((y,x)).data)
      for n in NEIGHBOURS:
        ny,nx = tuple(map(sum,zip((by,bx),n)))
        big_grid.set((ny,nx),scale[grid.at((y,x)).data][n[0]+1][n[1]+1])
  return big_grid


def part1(path):
  global start,grid,loop
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  grid.fill(file_data)
  grid.traverse(setStart)
  interpret_start_pipe()

  steps = 0
  steps = count_steps(start,steps)
  return steps


def part2(path):
  global start,grid,loop

  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  grid.fill(file_data)
  grid.traverse(setStart)
  
  interpret_start_pipe()
  count_steps(start,0)
  
  grid.traverse(clear_trash)
  big_grid = Grid()
  big_grid = scale_grid(grid,big_grid)

  # Elim any edge pieces and any direct neighbours touching the edges
  seen = set()
  for y in range(big_grid.height):
    for x in range(big_grid.width):
        
      queue = [(y,x)]
      while len(queue):
        qy,qx = queue.pop()
        if ((qy-1)/3,(qx-1)/3) in loop:
          continue

        if big_grid.at((qy,qx)).data == '.' or big_grid.at((qy,qx)).data == ',':
          flag = False
          for n in CARDINAL_NEIGHBOURS:
            ny,nx = tuple(map(sum,zip((qy,qx),n)))
            if not big_grid.in_bounds((ny,nx)):
              flag = True
              continue

            if ((ny-1)/3,(nx-1)/3) in loop:
              continue

            if big_grid.at((ny,nx)).data == '0':
              flag = True
            
            if big_grid.at((ny,nx)).data == '.' or big_grid.at((qy,qx)).data == ',':
              if not ((ny,nx) in seen):
                seen.add((ny,nx))
                queue.append((ny,nx))

          if flag:
            big_grid.set((qy,qx),'0')

  count = 0
  for y in range(big_grid.height):
    for x in range(big_grid.width):
      if big_grid.at((y,x)).data == '.':
        count += 1
  return count
      


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")