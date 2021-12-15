from collections import defaultdict
from math import ceil
from reused import arguments, read_file

PATH = "2021/day14/test.txt"

def make_replacements(template,replacements):
  new_template = []
  for i in range(len(template) - 1):
      if template[i] + template[i+1] in replacements:
        new_template.append(template[i])
        new_template.append(replacements[template[i] + template[i+1]])
  new_template.append(template[-1])
  return new_template

def get_input(file_data):
  template = [_ for _ in file_data[0]]
  replacements = {}
  for line in file_data[2:]:
    key,val = line.split(" -> ")
    replacements[key] = val
  return template, replacements

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  template,replacements = get_input(file_data)

  for _ in range(10):
    template = make_replacements(template,replacements)

  counts = defaultdict(int)
  for el in template:
    counts[el] += 1

  return max(counts.values()) - min(counts.values())


def replace(polymer_occurances,replacements):
  new_occurances = defaultdict(int)
  for key in polymer_occurances.keys():
    count = polymer_occurances[key]
    if (key in replacements):
      key1 = key[0] + replacements[key]
      key2 = replacements[key] + key[1]
      new_occurances[key1] += count
      new_occurances[key2] += count
  return new_occurances


def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  template, replacements = get_input(file_data)

  polymer_occurances = defaultdict(int)
  for i in range(len(template)-1):
    key = template[i] + template[i+1]
    polymer_occurances[key] += 1

  for _ in range(40):
    polymer_occurances = replace(polymer_occurances,replacements)

  counts = defaultdict(int)
  for pair in polymer_occurances:
    counts[pair[0]] += polymer_occurances[pair]/2
    counts[pair[1]] += polymer_occurances[pair]/2

  return ceil(max(counts.values())) - ceil(min(counts.values()))


if __name__ == "__main__":
  print(arguments(part1, part2))
  print("\n")