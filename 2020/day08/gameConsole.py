from reused import arguments, read_file
import re, copy, sys

PATH="2020/day08/input.txt"

OPERATIONS=["jmp","acc","nop"]
class int_code_machine():
  def __init__(self,insructions):
    self.accumulator = 0
    self.instructions = insructions
    self.instruction_counts = [0]*len(insructions)
    self.instruction_index = 0
    self.operation_parsers = {
      OPERATIONS[0]: self.parse_jmp,
      OPERATIONS[1]: self.parse_acc,
      OPERATIONS[2]: self.parse_nop
    }

  def get_sign_value (self,value):
    sign = re.match(r"(\+|-)",value).groups()[0]
    value = re.split(r"\+|-",value)[1]
    return (sign,value)

  def parse_jmp(self,value):
    (sign, value) = self.get_sign_value(value)

    if (sign == "+"):
      self.instruction_index += int(value)
    elif(sign == "-"):
      self.instruction_index -= int(value)

  def parse_acc(self,value):
    (sign, value) = self.get_sign_value(value)

    if (sign == "+"):
      self.accumulator += int(value)
    elif (sign == "-"):
      self.accumulator -= int(value)

    self.instruction_index +=1

  def parse_nop(self,value):
    self.instruction_index +=1
    pass

  def parse_instructions(self,debug = False):
    if (self.instruction_index >= len(self.instructions)):
      if (debug):
        return (self.accumulator,True)
      return self.accumulator

    curr_instruction = self.instructions[self.instruction_index]

    if (self.instruction_counts[self.instruction_index] > 0):
      if (debug):
        return (self.accumulator,False)
      return self.accumulator
    self.instruction_counts[self.instruction_index] += 1

    [operation,value] = curr_instruction.split()
    self.operation_parsers[operation](value)

    return self.parse_instructions(debug=True)
    
def tweak_boot_code(boot_code,index):
  while(True):
    index+=1
    if (index >= len(boot_code)):
      return (boot_code,index)

    if (OPERATIONS[0] in boot_code[index]):
      (op,value) = boot_code[index].split()
      boot_code[index] = OPERATIONS[2] + " " + value
      return (boot_code,index)
    elif (OPERATIONS[2] in boot_code[index]):
      (op,value) = boot_code[index].split()
      boot_code[index] = OPERATIONS[0] + " " + value
      return (boot_code,index)

    
def part1(path):
  boot_code = read_file(path or PATH,return_type=str,strip=True)
  machine = int_code_machine(boot_code)
  print(machine.parse_instructions())

def part2(path):
  og_boot_code = read_file(path or PATH,return_type=str,strip=True)

  tweak_index = -1
  boot_code = copy.deepcopy(og_boot_code)

  while(True):
    machine = int_code_machine(boot_code)
    (acc,termination) = machine.parse_instructions(debug=True)
    if (termination):
      break
    (boot_code,tweak_index) = tweak_boot_code(copy.deepcopy(og_boot_code),tweak_index)
    if (tweak_index >= len (boot_code)):
      print("Something went wrong while tweaking")
      sys.exit()
  print(acc)


if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")