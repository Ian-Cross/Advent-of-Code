from reused import arguments, read_file
from functools import reduce
import operator

PATH = "2023/day06/test.txt"

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, split=" ")
  
  times = [int(x) for x in file_data.pop(0)[1:] if x != ""]
  distances = [int(x) for x in file_data.pop(0)[1:] if x != ""]
  
  num_winners = []
  for x in range(len(times)):
    winners = []
    for t in range(times[x] + 1):
      if t*(times[x]-t) > distances[x]:
        winners.append(t)
    num_winners.append(len(winners))
  return reduce(operator.mul,num_winners)

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, split=" ")
  
  time = int("".join([x for x in file_data.pop(0)[1:] if x != ""]))
  distance = int("".join([x for x in file_data.pop(0)[1:] if x != ""]))
  
  winners = []
  for t in range(time + 1):
    if t*(time-t) > distance:
      winners.append(t)
  return len(winners)

  


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")