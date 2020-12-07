from reused import arguments, read_file
import re, string

PATH="2020/day07/input.txt"

def define_rule(rule):
  rules = rule.split("contain")
  parent_node = re.split(r"bags?",rules[0])[0].strip()
  child_nodes = {}
  for child in re.split(r",|\.",rules[1]):
    child = child.strip()
    if (child != ""):
      count = re.match("([0-9]+)",child)
      name = re.match("[0-9] ([a-z ]+)",child)
      if (count is not None):
        count = count.groups()[0]
      if (name is not None):
        name = name.groups()[0]
      
      if (name is not None and count is not None):
        child_nodes[re.split(r"bags?",name)[0].strip()] = count.strip()
  return (parent_node,child_nodes)

def check_inner_bags(rules,curr_key,matching_bag,level):
  for child in rules[curr_key]:
    if (child == matching_bag):
      return True
    elif (check_inner_bags(rules,child,matching_bag,level+1)):
      return True
      
  return False

def match_inner_bags(rules,matching_bag):
  count = 0
  for key in rules:
    if (check_inner_bags(rules,key,matching_bag,1)):
      count+=1
  return count

def count_inner_bags(rules,root):
  count = 1
  for child in rules[root]:
    count += int(rules[root][child]) * count_inner_bags(rules,child)
  return count
  

def part1(path):
  luggage_rules = read_file(path or PATH,return_type=str,strip=True)
  
  rules = {}
  for rule in luggage_rules:
    (parent,children) = define_rule(rule)
    rules[parent] = children

  print(match_inner_bags(rules,"shiny gold"))


def part2(path):
  luggage_rules = read_file(path or PATH,return_type=str,strip=True)

  rules = {}
  for rule in luggage_rules:
    (parent,children) = define_rule(rule)
    rules[parent] = children

  print(count_inner_bags(rules,"shiny gold")-1)

if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")