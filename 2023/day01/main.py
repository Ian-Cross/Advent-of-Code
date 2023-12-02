from reused import arguments, read_file
import re

PATH = "2023/day1/test.txt"

nums = {'one': 1,"two": 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9}

def process(line):
  newline = line
  word_number_index_pairs = {}
  for key in nums:
    if key in newline:
      matching_indices = [match.start() for match in re.finditer(key,newline)]
      for index in matching_indices:
        word_number_index_pairs[index] = key

  offset = 0
  keys = list(word_number_index_pairs.keys())
  keys.sort()

  for idx in keys:
    newline = \
      newline[:idx+offset+len(word_number_index_pairs[idx])] + \
      str(nums[word_number_index_pairs[idx]]) + \
      newline[idx+offset+len(word_number_index_pairs[idx]):]
    
    offset+=1

  return newline

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)

  sum = 0
  for line in file_data:
    first = 0
    last = 0
    for c in line:
      if first == 0 and c.isdigit():
        first = c
        continue
      if c.isdigit():
        last = c

    if last == 0:
      last = first

    sum += int(f"{first}{last}")

  return sum

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)

  sum = 0
  for line in file_data:
    newline = process(line)
    first = 0
    last = 0

    for c in newline:
      if first == 0 and c.isdigit():
        first = c
        continue
      if c.isdigit():
        last = c

    if last == 0:
      last = first

    sum += int(f"{first}{last}")

  return sum



if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")