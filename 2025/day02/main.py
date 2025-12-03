from reused import arguments, read_file
import re

PATH = "2025/day02/test.txt"

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, split=",")[0]
  
  total = 0
  for id in file_data:
    a,b = id.split("-")
    for x in range(int(a), int(b)+1):
      total += x if id[:len(id)//2] == id[len(id)//2:] else 0
  return total

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, split=",")[0]
  
  total = 0
  for id in file_data:
    a,b = id.split("-")
    for x in range(int(a), int(b)+1):
      if re.match(r"^(.+)\1+$", str(x)):
        total += x

  return total


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")