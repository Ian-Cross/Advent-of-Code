from reused import arguments, read_file
from common.numbers.lowestCommonMultiple import lcm
import re

PATH = "2023/day08/test.txt"

def run_route(route, turns, root, steps, exit):
  for c in route:
    root = turns[root][1 if c == 'R' else 0]
    steps += 1
    if exit():
      return root,steps
  return root,steps


def breakdown_rules(rules):
  turns = {}
  for line in rules.split("\n"):
    start,left,right = [x for x in re.split(" |=|\(|\,|\)",line) if x != ""]
    turns[start] = (left,right)
  return turns


def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, as_one=True,split="\n\n")
  
  route, rules = file_data
  turns = breakdown_rules(rules)

  root = 'AAA'
  steps = 0
  while 1:
    root,steps = run_route(route, turns, root, steps, lambda: root=='ZZZ')
    if root == 'ZZZ':
      break

  return steps

  

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, as_one=True,split="\n\n")
  
  route, rules = file_data
  turns = breakdown_rules(rules)

  roots = [key for key in turns.keys() if re.match('..A',key)]

  root_steps = []
  for root in roots:
    steps = 0
    while 1:
      root,steps = run_route(route, turns, root, steps, lambda: re.match("..Z",root))
      if re.match("..Z",root):
        break
    root_steps.append(steps)

  return lcm(root_steps)


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")