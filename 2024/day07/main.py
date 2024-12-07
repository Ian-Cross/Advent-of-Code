from reused import arguments, read_file
from common.numbers.toBase import to_base
from copy import copy
from operator import add, mul
from tqdm import tqdm

PATH = "2024/day07/test.txt"

def evaluation(equation, operators):
  for i in range(pow(len(operators),len(equation['right'])-1)):
    b = to_base(i, len(operators), len(equation['right']) - 1)
    rhs = copy(equation['right'])
    ans = rhs.pop(0)
    for j in b:
      ans = operators[int(j)](ans, rhs.pop(0))
    if ans == equation['left']:
      return True
  return False

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  equations = []
  for line in file_data:
    equation = {}
    equation["left"], equation["right"] = line.split(':')
    equation['left'] = int(equation['left'].strip())
    equation['right'] = [int(_) for _ in equation['right'].strip().split(' ')]
    equations.append(equation)

  operators = [add, mul]
  valid = []
  for equation in equations:
    if evaluation(equation, operators):
      valid.append(equation['left'])
  return sum(valid)

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)

  equations = []
  for line in file_data:
    equation = {}
    equation["left"], equation["right"] = line.split(':')
    equation['left'] = int(equation['left'].strip())
    equation['right'] = [int(_) for _ in equation['right'].strip().split(' ')]
    equations.append(equation)
  
  def cat(a, b):
    return int(str(a) + str(b))
  
  operators = [add, mul, cat]
  valid = []

  for equation in tqdm(equations):
    if evaluation(equation, operators):
      valid.append(equation['left'])
  return sum(valid)


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")