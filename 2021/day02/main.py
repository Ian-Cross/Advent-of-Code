from reused import arguments, read_file

PATH = "2021/day02/test.txt"

def part1(path):
  inputs = read_file(path or PATH, return_type=str, strip=True,split=" ")
  depth, horz = 0, 0

  for command in inputs:
    magnitude = int(command[1])
    if (command[0] == "forward"):
      horz += magnitude
    if (command[0] == "backward"):
       horz -= magnitude
    if (command[0] == "up"):
      depth -= magnitude
    if (command[0] == "down"):
      depth += magnitude
  
  print(depth*horz)
  pass

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True,split=" ")

  horz = 0
  depth = 0
  aim = 0

  for command in file_data:
    if (command[0] == "forward"):
      horz += int(command[1])
      depth += aim*int(command[1])
    if (command[0] == "backward"):
      horz -= int(command[1])
      depth -= aim*int(command[1])
    if (command[0] == "up"):
      aim -= int(command[1])
    if (command[0] == "down"):
      aim += int(command[1])
  
  print(depth*horz)
  pass


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")