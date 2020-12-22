from reused import arguments, read_file
import sys

PATH="2020/day18/input.txt"

OPERATIONS = ["+","*"]
OPEN_BRACKET = "("
CLOSE_BRACKET = ")"

class Equation():
  def __init__(self,equation):
    self.equation = equation.replace(" ","")
    self.value_stack = [0]
    self.operation_stack = [None]
    self.curr_value = -1
    self.curr_opperation = OPERATIONS[0]
    self.answer = 0
    pass

  def __str__(self):
      return self.equation + "=" + str(self.answer)

  def apply(self):
    try:
      if self.curr_opperation == OPERATIONS[0]:
        self.value_stack[-1] += int(self.curr_value)
      elif self.curr_opperation == OPERATIONS[1]:
        self.value_stack[-1] *= int(self.curr_value)
    except ValueError:
      print("Failed to convert a value to integer in the equation",self.curr_value)
      sys.exit()

  def evaluate(self):
    for char in self.equation:
      self.curr_value = char
      if self.curr_value.isnumeric():
        self.apply()
      elif self.curr_value in OPERATIONS:
        self.curr_opperation = self.curr_value
      elif self.curr_value == OPEN_BRACKET:
        self.operation_stack.append(self.curr_opperation)
        self.value_stack.append(0)
        self.curr_opperation = OPERATIONS[0]
      elif self.curr_value == CLOSE_BRACKET:
        self.curr_value = self.value_stack.pop()
        self.curr_opperation = self.operation_stack.pop()
        self.apply()
    self.answer = self.value_stack[0]

  def evaluate_w_presidence(self):
    for char in self.equation:
      self.curr_value = char
      if char.isnumeric():
        if self.curr_opperation == OPERATIONS[0]:
          self.value_stack[-1] += int(self.curr_value)

      elif self.curr_value == OPERATIONS[1]:
        if self.operation_stack[-1] == OPERATIONS[1]:
          self.operation_stack.pop()
          self.curr_value = self.value_stack.pop()
          self.value_stack[-1] *= self.curr_value
        self.operation_stack.append(OPERATIONS[1])
        self.curr_opperation = OPERATIONS[0]
        self.value_stack.append(0)
      
      elif self.curr_value == OPERATIONS[0]:
        self.curr_opperation = OPERATIONS[0]

      elif self.curr_value == OPEN_BRACKET:
        self.operation_stack.append(self.curr_opperation)
        self.curr_opperation = OPERATIONS[0]
        self.value_stack.append(0)

      elif self.curr_value == CLOSE_BRACKET:
        self.curr_value = self.value_stack.pop()
        self.curr_opperation = self.operation_stack.pop()
        self.apply()

        if (self.curr_opperation == OPERATIONS[1]):          
          self.curr_value = self.value_stack.pop()
          self.curr_opperation = self.operation_stack.pop()
          self.apply()
    
    if (len(self.value_stack) > 1):
      for i in self.value_stack:
        self.curr_value = self.value_stack.pop()
        self.curr_opperation = self.operation_stack.pop()
        self.apply()
    
    self.answer = self.value_stack[0]


def part1(path):
  equations = read_file(path or PATH,return_type=str,strip=True)

  sum = 0
  for equation in equations:
    equation = Equation(equation)
    equation.evaluate()
    # print(equation)
    sum += equation.answer
  print(sum)
  

def part2(path):
  equations = read_file(path or PATH,return_type=str,strip=True)
  
  sum = 0
  for equation in equations:
    equation = Equation(equation)
    equation.evaluate_w_presidence()
    # print(equation)
    sum += equation.answer
  print(sum)

if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")