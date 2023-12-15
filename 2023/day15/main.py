from reused import arguments, read_file
import re

PATH = "2023/day15/test.txt"

def hash(str):
  curr = 0
  for c in str:
    curr += ord(c)
    curr *= 17
    curr = curr % 256
  return curr

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, split=',')
  
  total = 0
  for line in file_data[0]:
    total += hash(line)
  return total


def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, split=',')
  
  total = 0
  hashmap = [[] for _ in range(256)]

  for line in file_data[0]:
    op = line[-1] if line[-1] == '-' else line[-2]
    breakdown = re.split("=|-",line)
    breakdown.append(hash(breakdown[0]))
    index = -1
    
    for i,lens in enumerate(hashmap[breakdown[2]]):
      if lens['id']== breakdown[0]:
        index = i

    if op == '-':
      if index == -1:
        continue
      else:
        hashmap[breakdown[2]].pop(index)
    elif op == '=':
      if index == -1:
        hashmap[breakdown[2]].append({'id': breakdown[0], 'focal': int(breakdown[1])})
      else:
        hashmap[breakdown[2]][index]['focal'] = int(breakdown[1])

  total = 0
  for box in [{'num': i, 'lenses': x} for i,x in enumerate(hashmap) if len(x) > 0]:
    for j,lens in enumerate(box['lenses']):
      total += (j+1) * (box['num']+1) * lens['focal']
  return total


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")