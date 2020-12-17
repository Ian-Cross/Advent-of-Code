from reused import arguments, read_file
import sys, itertools

PATH="2020/day16/input.txt"

class Ticket_validator():
  def __init__(self):
    self.rules = {}
    pass

  def __str__(self):
    string = ""
    for rule in self.rules:
      string += rule + ": " + str(self.rules[rule]) + "\n"
    return string

  def parse_rules(self,rule):
    [attribute, ranges] = rule.split(":")
    [low_range,high_range] = ranges.strip().split(" or ")
    [low_low_range, low_high_range] = low_range.split('-')
    [high_low_range, high_high_range] = high_range.split('-')
    try:
      self.rules[attribute] = {
        "low": {
          "low": int(low_low_range),
          "high": int(low_high_range),
        }, 
        "high": {
          "low": int(high_low_range),
          "high": int(high_high_range)
        }
      }
    except ValueError:
      print("Something went wrong while parsing the rules, val not an int")
      sys.exit()

  def within_rules(self,val):
    for rule in self.rules:
      for ranges in self.rules[rule]:
        if (val >= self.rules[rule][ranges]["low"] and val <= self.rules[rule][ranges]["high"]):
          return True
    return False

  def follows_rule(self,rule,val):
    for ranges in rule:
      if (val >= rule[ranges]["low"] and val <= rule[ranges]["high"]):
          return True
    return False

  def match_keys(self,valid_tickets):
    matched_keys = {}
    for key in self.rules:
      matched_keys[key] = []
      for i in range(len(valid_tickets[0])):
        fail = False
        for ticket in valid_tickets:
          if (not self.follows_rule(self.rules[key],ticket[i])):
            fail = True
        if (not fail):
          matched_keys[key].append(i)
    return (matched_keys)

  def is_valid_ticket(self,ticket):
    ticket_breakdown = []
    for val in ticket.split(","):
      try:
        val = int(val)
        ticket_breakdown.append(val)
      except ValueError:
        print("Something wrong with a ticket, val is not an int")
        sys.exit()
      if (not self.within_rules(val)):
        return (None,False)
    return (ticket_breakdown,True)

def part1(path):
  ticket_specs = read_file(path or PATH,return_type=str,strip=True)

  validator = Ticket_validator()
  i = 0
  while (ticket_specs[i] != ""):
    validator.parse_rules(ticket_specs[i])
    i += 1

  i += 2
  my_ticket = ticket_specs[i]
  i += 3

  sum = 0
  while (i < len(ticket_specs)):
    for val in ticket_specs[i].split(","):
      try:
        val = int(val)
      except ValueError:
        print("Something wrong with a ticket, val is not an int")
        sys.exit()
      if (not validator.within_rules(val)):
        sum += val
    i+=1

  print(sum)
  

def part2(path):
  ticket_specs = read_file(path or PATH,return_type=str,strip=True)
  validator = Ticket_validator()

  ## Parsing the File ##

  # Getting the rules
  i = 0
  while (ticket_specs[i] != ""):
    validator.parse_rules(ticket_specs[i])
    i += 1
  i += 2

  # Breaking apart my ticket details
  ticket = ticket_specs[i].split(",")
  i += 3

  # exluding invalid tickets
  valid_tickets = []
  while (i < len(ticket_specs)):
    (ticket_specs[i], is_valid) = validator.is_valid_ticket(ticket_specs[i])
    if (is_valid):
      valid_tickets.append(ticket_specs[i])
    i+=1

  ## Reverse Engineering my ticket
  matched_keys = validator.match_keys(valid_tickets)

  i = 1
  taken = []
  reconstructed_ticket = {}
  while (i <= len(matched_keys)):
    for match in matched_keys:
      if (len(matched_keys[match]) == i):
        for option in matched_keys[match]:
          if (option not in taken):
            reconstructed_ticket[match] = int(ticket[option])
            taken.append(option)
            break
    i += 1

  sum = 1
  for el in reconstructed_ticket:
    if "departure" in el:
      sum *= reconstructed_ticket[el]
  print(sum)

if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")