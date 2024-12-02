from reused import arguments, read_file

PATH = "2024/day02/test.txt"

def part1(path):
  file_data = read_file(path or PATH, return_type=int, strip=True, split=" ")

  count = 0
  allowed_steps = [1, 2, 3]
  for line in file_data:

    steps = [line[i] - line[i+1] for i in range(len(line) - 1)]
    dir = steps[0] > 0

    if any([(
      (abs(step) not in allowed_steps) or 
      (dir != (step > 0))
    ) for step in steps]):
      continue

    count += 1

  return count

def part2(path):
  file_data = read_file(path or PATH, return_type=int, strip=True, split=" ")

  count = 0
  allowed_steps = [1, 2, 3]
  for line in file_data:
    lines = []
    lines.append(line)
    for x in range(len(line)):
      line_copy = line.copy()
      line_copy.pop(x)
      lines.append(line_copy)

    success = False
    for line in lines:

      steps = [line[i] - line[i+1] for i in range(len(line) - 1)]
      dir = steps[0] > 0

      if any([(
        (abs(step) not in allowed_steps) or 
        (dir != (step > 0))
      ) for step in steps]):
        continue

      success = True
      break

    if success:
      count += 1

  return count


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")