from reused import arguments, read_file

PATH = "2024/day02/test.txt"

def is_safe(line):
  allowed_steps = {1, 2, 3}
  steps = [line[i] - line[i+1] for i in range(len(line) - 1)]
  dir = steps[0] > 0

  return all(abs(step) in allowed_steps and (dir == (step > 0)) for step in steps)


def part1(path):
  file_data = read_file(path or PATH, return_type=int, strip=True, split=" ")

  count = 0
  for line in file_data:
    if is_safe(line):
      count += 1

  return count

def part2(path):
  file_data = read_file(path or PATH, return_type=int, strip=True, split=" ")

  count = 0
  for line in file_data:
    if any(is_safe(line[:i] + line[i+1:]) for i in range(len(line))):
      count += 1

  return count


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")