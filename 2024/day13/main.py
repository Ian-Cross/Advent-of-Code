from reused import arguments, read_file
import re

PATH = "2024/day13/test.txt"

def solve_equations(a, b, c):
  x = (c[1]*b[0]*-1 - c[0]*b[1]*-1) / (a[0]*b[1] - a[1]*b[0])
  y = (((x * a[1]) - c[1])*-1) / b[1]
  return (x, y)

def verbose_solve_equations(a, b, c):
  print(f"x{a[0]} + y{b[0]} = {c[0]}")
  print(f"x{a[1]} + y{b[1]} = {c[1]}")
  print()
  print(f"x{a[0]} - {c[0]} = -y{b[0]}")
  print(f"x{a[1]} - {c[1]} = -y{b[1]}")
  print()
  print(f" - (x{a[0]} - {c[0]}) / {b[0]} = y")
  print(f" - (x{a[1]} - {c[1]}) / {b[1]} = y")
  print()
  print(f"(x{a[0]} - {c[0]}) / {b[0]} = (x{a[1]} - {c[1]}) / {b[1]}")
  print()
  print(f"(x{a[0]} - {c[0]}) * {b[1]} = (x{a[1]} - {c[1]}) * {b[0]}")
  print()
  print(f"(x{a[0]*b[1]} - {c[0]*b[1]}) = (x{a[1]*b[0]} - {c[1]*b[0]})")
  print()
  print(f"x{a[0]*b[1]} - x{a[1]*b[0]} = {c[1]*b[0]*-1 - c[0]*b[1]*-1}")
  print()
  print(f"x{a[0]*b[1] - a[1]*b[0]} = {c[1]*b[0]*-1 - c[0]*b[1]*-1}")
  print()
  print(f"x = {c[1]*b[0]*-1 - c[0]*b[1]*-1} / {a[0]*b[1] - a[1]*b[0]}")
  print()
  print(f"x = {(c[1]*b[0]*-1 - c[0]*b[1]*-1) / (a[0]*b[1] - a[1]*b[0])}")
  x = (c[1]*b[0]*-1 - c[0]*b[1]*-1) / (a[0]*b[1] - a[1]*b[0])
  print()
  print(f"y =  - (x{a[1]} - {c[1]}) / {b[1]}")
  print()
  print(f"y = -({(c[1]*b[0]*-1 - c[0]*b[1]*-1) // (a[0]*b[1] - a[1]*b[0]) * a[1]} - {c[1]}) / {b[1]}")
  print()
  print(f"y = {(((c[1]*b[0]*-1 - c[0]*b[1]*-1) // (a[0]*b[1] - a[1]*b[0]) * a[1]) - c[1])*-1} / {b[1]}")
  print()
  print(f"y = {((((c[1]*b[0]*-1 - c[0]*b[1]*-1) / (a[0]*b[1] - a[1]*b[0]) * a[1]) - c[1])*-1) / b[1]}")
  y = (((x * a[1]) - c[1])*-1) / b[1]
  return (x, y)

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, split="\n\n", as_one=True)
  
  buttons = []

  for line in file_data:
    button = {}
    for item in line.split("\n"):
      items = [_ for _ in re.split(r":|,|\+| |\=", item) if _ != ""]
      if len(items) > 5:
        button[items[1]] = (int(items[3]), int(items[5]))
      else:
        button[items[0]] = (int(items[2]), int(items[4]))
    buttons.append(button)


  total_coins = 0
  for button in buttons:
    x,y = solve_equations(button['A'], button['B'], button['Prize'])
    if x.is_integer() and y.is_integer():
      total_coins += int(x)*3 + int(y)
  return total_coins

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, split="\n\n", as_one=True)
  
  buttons = []

  for line in file_data:
    button = {}
    for item in line.split("\n"):
      items = [_ for _ in re.split(r":|,|\+| |\=", item) if _ != ""]
      if len(items) > 5:
        button[items[1]] = (int(items[3]), int(items[5]))
      else:
        button[items[0]] = (int(items[2]) + 10**13, int(items[4]) + 10**13)
    buttons.append(button)


  total_coins = 0
  for button in buttons:
    x,y = solve_equations(button['A'], button['B'], button['Prize'])
    if x.is_integer() and y.is_integer():
      total_coins += int(x)*3 + int(y)
  return total_coins


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")