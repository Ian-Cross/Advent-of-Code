from reused import arguments, read_file
from common.grid import Grid,Square
from common.constants import NEIGHBOURS_MAP

PATH = "2023/day16/test.txt"
grid = Grid()
beams = []

def move_beam(i):
  global beams,visited
  if beams[i]['loc'] in visited:
    if beams[i]['dir'] in visited[beams[i]['loc']]:
      beams.pop(i)
      return
    else:
      visited[beams[i]['loc']].append(beams[i]['dir'])
  else:
    visited[beams[i]['loc']] = [beams[i]['dir']]

  el = grid.at(beams[i]['loc']).data

  if el == '/':
    if beams[i]['dir'] == 'n':
      beams[i]['dir'] = 'e'
    elif beams[i]['dir'] == 'e':
      beams[i]['dir'] = 'n'
    elif beams[i]['dir'] == 's':
      beams[i]['dir'] = 'w'
    elif beams[i]['dir'] == 'w':
      beams[i]['dir'] = 's'
  
  elif el == '\\':
    if beams[i]['dir'] == 'n':
      beams[i]['dir'] = 'w'
    elif beams[i]['dir'] == 'w':
      beams[i]['dir'] = 'n'
    elif beams[i]['dir'] == 's':
      beams[i]['dir'] = 'e'
    elif beams[i]['dir'] == 'e':
      beams[i]['dir'] = 's'

  elif el == '|' and (beams[i]['dir'] == 'e' or beams[i]['dir'] == 'w'):
    beams[i]['dir'] = 's'
    beams.append({'loc': beams[i]['loc'],'dir': 'n'})

  elif el == '-' and (beams[i]['dir'] == 's' or beams[i]['dir'] == 'n'):
    beams[i]['dir'] = 'w'
    beams.append({'loc': beams[i]['loc'],'dir': 'e'})

  if grid.in_bounds(beams[i]['loc'],NEIGHBOURS_MAP[beams[i]['dir']]):
    beams[i]['loc'] = tuple(map(sum,zip(beams[i]['loc'],NEIGHBOURS_MAP[beams[i]['dir']])))
  else:
    beams.pop(i)
    return

def part1(path):
  global grid,beams,visited
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  grid.fill(file_data)

  visited = {}
  beams = [{'loc':(0,0),'dir': 'e'}]
  while len(beams):
    i = 0
    while i < len(beams):
      move_beam(i)
      i += 1

  return len(visited)

def part2(path):
  global grid,beams,visited
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  grid.fill(file_data)

  starting_options = []
  for i in range(1,grid.width):
    starting_options.append({'loc':(0, i),'dir': 's'})
    starting_options.append({'loc':(grid.height-1, i),'dir': 'n'})
  for i in range(1,grid.height):
    starting_options.append({'loc':(i, 0),'dir': 'e'})
    starting_options.append({'loc':(i, grid.width-1),'dir': 'w'})

  max_energy = 0
  for start in starting_options:
    visited = {}
    beams = [start]
    while len(beams):
      i = 0
      while i < len(beams):
        move_beam(i)
        i += 1

    if len(visited) > max_energy:
      max_energy = len(visited)
  
  return max_energy


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")