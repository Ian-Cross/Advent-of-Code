from reused import arguments, read_file
from common.numbers import to_base

PATH = "2023/day12/test.txt"
saved_matches = {}

def compute(report,check,i,j,current):
  global saved_matches
  key = (i,j,current)
  if key in saved_matches:
    return saved_matches[key]
  
  if i == len(report):
    if j == len(check) and current == 0:
      return 1
    elif j == len(check)-1 and current == check[j]:
      return 1
    else:
      return 0
    
  ans = 0
  for c in ['.','#']:
    if report[i] != c and report[i] != '?':
      continue

    if c == '.' and current == 0:
      ans += compute(report,check,i+1,j,0)
    elif c == '.' and current > 0 and j < len(check) and check[j] == current:
      ans += compute(report,check,i+1,j+1,0)
    elif c == '#':
      ans += compute(report,check,i+1,j,current+1)

  saved_matches[key] = ans
  return ans

def part1(path):
  global saved_matches
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  sum = 0
  for line in file_data:
    saved_matches = {}
    report,backup = line.split(" ")
    check = [int(_) for _ in backup.split(',')]
    report = list(report)
    sum += compute(report,check,0,0,0)
  return sum

def part2(path):
  global saved_matches
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  sum = 0
  for line in file_data:
    saved_matches = {}
    report,check = line.split(" ")

    report = '?'.join([report,report,report,report,report])
    check = ','.join([check,check,check,check,check])

    check = [int(_) for _ in check.split(',')]
    report = list(report)

    sum += compute(report,check,0,0,0)
  return sum


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")