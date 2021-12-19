from reused import arguments, read_file
import re

PATH = "2021/day17/input.txt"

def overshot(x_pos,y_pos,target):
  left,top,right,bottom = target
  if x_pos > right:
    return True
  if y_pos < bottom:
    return True
  return False

def inTarget(x_pos,y_pos,target):
  left,top,right,bottom = target
  if x_pos > right or x_pos < left:
    return False
  if y_pos > top or y_pos < bottom:
    return False
  return True

def shoot(y_v, x_v, target):
  # print(f"Shooting at {x_v} {y_v}")
  x_pos,y_pos = 0,0
  max_y_pos = 0
  while not overshot(x_pos,y_pos,target):
    # print(f"\tcurrent position {x_pos} {y_pos}")
    y_pos += y_v
    y_v -= 1
    max_y_pos = max(max_y_pos,y_pos)

    x_pos += x_v
    if x_v > 0:
      x_v -= 1
    
    if (inTarget(x_pos,y_pos,target)):
      return True,max_y_pos
  # print("\tOvershot")
  return False,0
    

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)

  left,right,top,bottom = 0,0,0,0  
  try: 
    search = re.findall("([x|y]=(-?[0-9]*)..(-?[0-9]*))",file_data[0])
    if len(search) != 2:
      return
    left,right = int(search[0][1]),int(search[0][2])
    bottom,top = int(search[1][1]),int(search[1][2])
  except:
    return
  target = left,top,right,bottom

  x_distance = right
  step = 1
  while x_distance - step >= 0:
    x_distance -= step
    step += 1
  max_v_x = step-1

  max_y_pos = 0
  count = 0
  for y_v in range(-200,200):
    for x_v in range(-200,200):
      hit, _max_y_pos = shoot(y_v,x_v,target)
      if hit:
        print(f'{x_v},{y_v} ')
        count += 1
        max_y_pos = max(_max_y_pos, max_y_pos)

  return max_y_pos,count

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  print(file_data)
  pass


if __name__ == "__main__":
  print(arguments(part1, part2))
  print("\n")