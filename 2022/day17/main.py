from reused import arguments, read_file

PATH = "2022/day17/test.txt"

def part1(path):
  file_data = read_file(path or PATH, return_type=int, strip=True)
  print(file_data)
  pass

def part2(path):
  file_data = read_file(path or PATH, return_type=int, strip=True)
  print(file_data)
  pass


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")