from reused import arguments, read_file

PATH = "2025/day05/test.txt"

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, as_one=True)
  ranges,ingredients = file_data.split("\n\n")
  ranges = [[int(i) for i in r.split("-")] for r in ranges.split("\n")]
  ingredients = [int(i) for i in ingredients.split("\n")]

  return sum(any(r1 <= i <= r2 for r1, r2 in ranges) for i in ingredients)

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, as_one=True)
  ranges,_ = file_data.split("\n\n")
  ranges = [[int(i) for i in r.split("-")] for r in ranges.split("\n")]
  
  merged = []
  ranges.sort()
  for r1,r2 in ranges:
    if not merged or merged[-1][1] < r1 - 1:
      merged.append([r1,r2])
    else:
      merged[-1][1] = max(merged[-1][1], r2)

  return sum(r2 - r1 + 1 for r1,r2 in merged)

if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")