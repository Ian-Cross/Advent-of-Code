from reused import arguments, read_file
import re
from collections import defaultdict

PATH = "2024/day05/test.txt"

def is_valid(update, sortOrder):
  for key in update:
    if key not in sortOrder:
      continue

    if any(update.index(value) <= update.index(key) for value in sortOrder[key] if value in update):
      return False
  return True


def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, as_one=True)
  
  rules, updates = file_data.split('\n\n')
  rules = [re.split(r",|\|", line) for line in rules.split('\n')]
  updates = [[int(_) for _ in re.split(r",|\|", line)] for line in updates.split('\n')]

  sortOrder = defaultdict(list)
  for rule in rules:
    sortOrder[int(rule[0])].append(int(rule[1]))

  return sum([update[len(update) // 2] for update in updates if is_valid(update, sortOrder)])

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, as_one=True)
  
  rules, updates = file_data.split('\n\n')
  rules = [re.split(r",|\|", line) for line in rules.split('\n')]
  updates = [[int(_) for _ in re.split(r",|\|", line)] for line in updates.split('\n')]

  sortOrder = defaultdict(list)
  for rule in rules:
    sortOrder[int(rule[0])].append(int(rule[1]))

  fixedUpdates = []
  for update in [update for update in updates if not is_valid(update, sortOrder)]:
    sortedUpdate = [update[0]]
    for key in update[1:]:
      if key not in sortOrder:
        sortedUpdate.append(key)
        continue

      for index, value in enumerate(sortedUpdate):
        if value in sortOrder[key]:
          sortedUpdate.insert(index, key)
          break
      else:
        sortedUpdate.append(key)
    fixedUpdates.append(sortedUpdate)

  return sum([update[len(update) // 2] for update in fixedUpdates])

if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")