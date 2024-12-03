from reused import arguments, read_file
import re

PATH = "2024/day03/test.txt"

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True,as_one=True)
  pattern = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")
  return sum(int(a) * int(b) for a, b in re.findall(pattern, file_data))

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, as_one=True)

  pattern = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do|don't)\(\)")
  matches = re.findall(pattern, file_data)
  
  res = 0
  enabled = True

  for a, b, c in matches:
    if c:
      enabled = (c == "do")
    elif enabled:
      res += int(a) * int(b)
      
  return res


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")