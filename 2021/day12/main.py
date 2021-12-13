from reused import arguments, read_file
from copy import deepcopy

PATH = "2021/day12/input.txt"
CAVE_PATHS = []

def find_path_part_1(caves,start,path):
  turns = caves[start]
  for turn in turns:
    if turn.islower() or turn == 'start':
      caves[start] = [_ for _ in turns if _ != turn]
      if turn in path:
        continue

    path.append(turn)
    if (turn == 'end'):
      CAVE_PATHS.append(path)
    else:
      find_path_part_1(deepcopy(caves),turn,deepcopy(path))
    path = path[:-1]

def build_map(file_data):
  caves = {}
  for line in file_data:
    (start,end) = line.split("-")
    if start in caves:
      caves[start].append(end)
    else:
      caves[start] = [end]

    if start == 'start' or end == 'end':
      continue

    if end in caves:
      caves[end].append(start)
    else:
      caves[end] = [start]
  return caves

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  caves = build_map(file_data)

  find_path_part_1(caves,'start',['start'])
  return len(CAVE_PATHS)

def has_double(path):
  counts = {}
  for item in path:
    if (item.islower()):
      if item in counts:
        counts[item] += 1
      else:
        counts[item] = 1
  for count in counts:
    if counts[count] > 1:
      return True
  return False


def find_path_part_2(caves,start,path, depth):
  turns = caves[start]
  for turn in turns:
    if turn.islower():
      if turn == 'start':
        caves[start] = [_ for _ in turns if _ != turn]
        continue

      if (has_double(path)):
        caves[start] = [_ for _ in turns if _ != turn]
        if turn in path:
          continue

    path.append(turn)
    if (turn == 'end'):
      CAVE_PATHS.append(path)
    else:
      find_path_part_2(deepcopy(caves),turn,deepcopy(path),depth+1)
    path = path[:-1]

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  caves = build_map(file_data)

  # for cave in caves:
  #   print(cave, caves[cave])

  find_path_part_2(caves,'start',['start'],0)
  # for path in CAVE_PATHS:
  #   print(path)
  return len(CAVE_PATHS)


if __name__ == "__main__":
  print(arguments(part1, part2))
  print("\n")