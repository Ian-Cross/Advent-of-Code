from reused import arguments, read_file

PATH = "2021/day07/test.txt"

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  positions = [int(pos) for pos in file_data[0].split(",")]
  min_sum = 999999999

  for i in range(min(positions),max(positions)+1):
    sum = 0
    for pos in positions:
      sum += abs(pos - i)
    if (sum < min_sum):
      min_sum = sum
  return min_sum



def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  positions = [int(pos) for pos in file_data[0].split(",")]
  min_sum = 999999999

  for i in range(min(positions),max(positions)+1):
    sum = 0
    for pos in positions:
      sum += ((abs(pos - i) * (abs(pos - i) + 1)) / 2)

    if (sum < min_sum):
      min_sum = sum
  return int(min_sum)


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")