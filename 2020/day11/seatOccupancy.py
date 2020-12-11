from reused import arguments, read_file
import copy

PATH="2020/day11/input.txt"
NEIGHBOURS = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]

def isEqual(a,b):
  for a_x,b_x in zip(a,b):
    for a_y,b_y in zip(a_x,b_x):
      if (a_y != b_y):
        return False
  return True

def count_occupied(seat_array):
  occupied = 0
  for y in seat_array:
    for x in y:
      if (x == "#"):
        occupied += 1
  return occupied

def has_visible_neighbours(seat_array,y,x):
  og_y,og_x = y,x
  for neighbour in NEIGHBOURS:
    y,x = og_y,og_x
    while(True):
      if ((y + neighbour[0]) < 0 or (y + neighbour[0]) >= len(seat_array)):
        break
      if ((x + neighbour[1]) < 0 or (x + neighbour[1]) >= len(seat_array[0])):
        break
      if (seat_array[y + neighbour[0]][x + neighbour[1]] == "#"):
        return True
      elif (seat_array[y + neighbour[0]][x + neighbour[1]] == "L"):
        break
      y += neighbour[0]
      x += neighbour[1]
  return False

def has_neighbours(seat_array,y,x):
  for neighbour in NEIGHBOURS:
    if (0 <= (y + neighbour[0]) < len(seat_array)):
      if (0 <= (x + neighbour[1]) < len(seat_array[0])):
        if (seat_array[y + neighbour[0]][x + neighbour[1]] == "#"):
          return True
  return False

def count_visible_neighbours(seat_array,y,x):
  neighbour_count = 0
  og_y,og_x = y,x
  for neighbour in NEIGHBOURS:
    y,x = og_y,og_x
    while(True):
      if ((y + neighbour[0]) < 0 or (y + neighbour[0]) >= len(seat_array)):
        break
      if ((x + neighbour[1]) < 0 or (x + neighbour[1]) >= len(seat_array[0])):
        break
      if (seat_array[y + neighbour[0]][x + neighbour[1]] == "L"):
        break
      if (seat_array[y + neighbour[0]][x + neighbour[1]] == "#"):
        neighbour_count += 1
        break
      y += neighbour[0]
      x += neighbour[1]
  return neighbour_count

def count_neighbours(seat_array,y,x):
  neighbour_count = 0
  for neighbour in NEIGHBOURS:
    if (0 <= (y + neighbour[0]) < len(seat_array)):
      if (0 <= (x + neighbour[1]) < len(seat_array[0])):
        if (seat_array[y + neighbour[0]][x + neighbour[1]] == "#"):
          neighbour_count += 1
  return neighbour_count

def print_generation(seat_array,new_seat_array):
  for y in range(len(seat_array)):
    for x in range(len(seat_array[y])):
      print(seat_array[y][x], end=" ")
    print()
  print()
  for y in range(len(new_seat_array)):
    for x in range(len(new_seat_array[y])):
      print(new_seat_array[y][x], end=" ")
    print()
  input()

def seat_persons(seat_array, generation, max_neighbours = 4, line_of_sight = False):
  new_seat_array = copy.deepcopy(seat_array)

  for y in range(len(seat_array)):
    for x in range(len(seat_array[y])):
      if (seat_array[y][x] == 'L'):
        if (line_of_sight):
          if (not has_visible_neighbours(seat_array,y,x)):
            new_seat_array[y][x] = "#"
        else:
          if (not has_neighbours(seat_array,y,x)):
            new_seat_array[y][x] = "#"
      if (seat_array[y][x] == '#'):
        if (line_of_sight):
          if (count_visible_neighbours(seat_array,y,x) >= max_neighbours):
            new_seat_array[y][x] = "L"
        else:
          if (count_neighbours(seat_array,y,x) >= max_neighbours):
            new_seat_array[y][x] = "L"

  # print_generation(seat_array,new_seat_array)
      
  if (isEqual(seat_array,new_seat_array)):
    return count_occupied(new_seat_array)
  else:
    return seat_persons(new_seat_array,generation+1, max_neighbours, line_of_sight)

def build_2d_array(seat_array):
  new_array = []
  for y in seat_array:
    new_row = []
    for x in y:
      new_row.append(x)
    new_array.append(new_row)
  return new_array

def part1(path):
  seat_array = read_file(path or PATH,return_type=str,strip=True)
  seat_array = build_2d_array(seat_array)

  print(seat_persons(seat_array, 0))

def part2(path):
  seat_array = read_file(path or PATH,return_type=str,strip=True)
  seat_array = build_2d_array(seat_array)

  print(seat_persons(seat_array, 0, max_neighbours = 5, line_of_sight=True))

if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")