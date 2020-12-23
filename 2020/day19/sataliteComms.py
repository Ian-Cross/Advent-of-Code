from reused import arguments, read_file
from re import fullmatch, compile
import sys

PATH="2020/day19/input.txt"

class Regex_Machine():
  def __init__(self):
    self.rules = {}
    pass

  def parse_rule(self,rule):
    rule_no = rule.split(": ")[0]
    rule_body = rule.split(": ")[1].replace('"', "")
    return (rule_no,rule_body)

  def add_rule(self,rule):
    rule_no,rule_body = self.parse_rule(rule)
    self.rules[rule_no] = rule_body

  def set_rule(self,key,value):
    self.rules[key] = value

  def convert_rules_to_regex(self,rule_no):
    string = "("
    rule = self.rules[rule_no].split()

    for value in rule:
      if value.isnumeric():
        string += self.convert_rules_to_regex(value)
      elif value.isalpha():
        string += value
      else:
        string += value

    return string + ")"

def part1(path):
  satelite_comms = read_file(path or PATH,return_type=str,strip=True)
  
  machine = Regex_Machine()
  i = 0
  while (True):
    if (satelite_comms[i] == ""):
      break
    machine.add_rule(satelite_comms[i])
    i += 1
  i+=1

  satelite_comms[i:]

  pattern_string = machine.convert_rules_to_regex("0")
  pattern = compile(pattern_string)

  valid_count = 0
  for message in satelite_comms:
    if (fullmatch(pattern,message)):
      valid_count += 1
  print(valid_count)
    

def part2(path):
  satelite_comms = read_file(path or PATH,return_type=str,strip=True)
  machine = Regex_Machine()
  i = 0
  while (True):
    if (satelite_comms[i] == ""):
      break
    machine.add_rule(satelite_comms[i])
    i += 1
  i+=1

  satelite_comms[i:]

  # Issue is new recursive rules,
  #   rule 8: "42 | 42 8"
  #     Matches an infinite string of repeated rule 42
  #     regex equivalent is "42 +"
  machine.set_rule("8","42 +")

  #   rule 11: "42 31 | 42 11 31"
  #     Matches an infinite string of repeated rule 42 followed by a rule 31
  #   rule 11: "42 + 31 +"
  #     very close, but needs to be even 42 & 31
  #   rule 11: "42 (42 .. 31)? 31 "
  #     nested repeated optional pairs will work, not a universal solution, will miss larger strings
  machine.set_rule("11","42 ( 42 ( 42 ( 42 ( 42 ( 42 ( 42 ( 42 ( 42 ( 42 ( 42 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31")

  pattern_string = machine.convert_rules_to_regex("0")
  pattern = compile(pattern_string)

  valid_count = 0
  for message in satelite_comms:
    if (fullmatch(pattern,message)):
      valid_count += 1
  print(valid_count)


if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")