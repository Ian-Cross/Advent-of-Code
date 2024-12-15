from reused import arguments, read_file
import re
from common.constants import CARDINAL_NEIGHBOURS

PATH = "2024/day14/test.txt"

robots = []

h,w = 103,101
# h,w = 7,11
STEPS = 100

def part1(path):
  global tiles
  file_data = read_file(path or PATH, return_type=str, strip=True)

  for line in file_data:
    pos,vel = line.split(" ")
    pos = tuple([int(_) for _ in re.split(f",|=",pos)[1:]])
    vel = tuple([int(_) for _ in re.split(f",|=",vel)[1:]])
    robots.append({
      "pos": pos,
      "vel": vel
    })
  
  for _ in range(STEPS):
    for robot in robots:
      pos,vel = robot['pos'],robot['vel']
      new_pos = ((pos[0]+vel[0])%w,(pos[1]+vel[1])%h)
      robot['pos'] = new_pos

  quads = [0,0,0,0]
  for robot in robots:
    pos = robot['pos']
    if pos[0] < w//2 and pos[1] < h//2:
      quads[0] += 1
    elif pos[0] < w//2 and pos[1] > h//2:
      quads[1] += 1
    elif pos[0] > w//2 and pos[1] < h//2:
      quads[2] += 1
    elif pos[0] > w//2 and pos[1] > h//2:
      quads[3] += 1

  return quads[0]*quads[1]*quads[2]*quads[3]

def is_tree(robots, i):
  connected = 0
  seen = set()
  positions = [robot['pos'] for robot in robots]

  for robot in robots:
    if robot['pos'] in seen:
      continue

    for n in CARDINAL_NEIGHBOURS:
      new_pos = ((robot['pos'][0]+n[0]),(robot['pos'][1]+n[1]))
      if 0 <= new_pos[0] < w and 0 <= new_pos[1] < h:
        if new_pos in positions:
          seen.add(new_pos)
          connected += 1
  
  if (connected >= len(robots) // 2):
    return True
  return False

def part2(path):
  global tiles
  file_data = read_file(path or PATH, return_type=str, strip=True)

  for line in file_data:
    pos,vel = line.split(" ")
    pos = tuple([int(_) for _ in re.split(f",|=",pos)[1:]])
    vel = tuple([int(_) for _ in re.split(f",|=",vel)[1:]])
    robots.append({
      "pos": pos,
      "vel": vel
    })
  
  steps = 0
  while not is_tree(robots, steps):
    for robot in robots:
      pos,vel = robot['pos'],robot['vel']
      new_pos = ((pos[0]+vel[0])%w,(pos[1]+vel[1])%h)
      robot['pos'] = new_pos
    steps += 1
  
  return steps


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")