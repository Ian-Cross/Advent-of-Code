from reused import arguments, read_file
from collections import defaultdict

PATH = "2024/day01/test.txt"

def part1(path):
  file_data = read_file(path or PATH, return_type=int, strip=True,split="   ")
  listA, listB = zip(*file_data)
  sum = 0
  for a, b in zip(sorted(listA), sorted(listB)):
    sum += abs(a - b)

  return sum
  

def part2(path):
  file_data = read_file(path or PATH, return_type=int, strip=True, split="   ")
  listA, listB = zip(*file_data)

  occurances = defaultdict(int)
  for b in listB:
    occurances[b] += 1

  return sum(a * occurances[a] for a in listA)


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")