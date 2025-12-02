from reused import arguments, read_file

PATH = "2025/day01/test.txt"

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  dial = 50
  total = 0
  for line in file_data:
    dir, value = line[0], int(line[1:])
    if dir == "L":
      dial -= value
    elif dir == "R":
      dial += value
    dial = dial % 100
    if dial == 0:
      total += 1
  return total


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    dial = 50
    total = 0
    for line in file_data:
        dir, value = line[0], int(line[1:])
        if dir == "L":
            total += ((dial - 1) // 100 - (dial - value - 1) // 100)
            dial -= value
        elif dir == "R":
            total += ((dial + value) // 100) - (dial // 100)
            dial += value
        dial = dial % 100
    return total


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")