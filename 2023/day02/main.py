from reused import arguments, read_file
from collections import defaultdict
from functools import reduce
import operator

PATH = "2023/day02/test.txt"

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)

  goal = { "red": 12, "green": 13, "blue": 14}
  sum = 0

  for line_num,line in enumerate(file_data):
    game_possible = True
    
    for stage in line.split(":")[1].split(";"):
      for pull in [cube_pull.strip() for cube_pull in stage.split(",")]:
        [amount,colour] = pull.split(" ")
        if int(amount) > goal[colour]:
          game_possible = False

    if game_possible:
      sum += int(line_num+1)
      
  return sum


def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)

  sum = 0
  for line in file_data:
    min_stats = defaultdict(lambda: 0)
    for stage in line.split(":")[1].split(";"):      
      for pull in [cube_pull.strip() for cube_pull in stage.split(",")]:
        [amount,colour] = pull.split(" ")
        if int(amount) > min_stats[colour]:
          min_stats[colour] = int(amount)
        
    sum += reduce(operator.mul,min_stats.values(),1)

  return sum


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")