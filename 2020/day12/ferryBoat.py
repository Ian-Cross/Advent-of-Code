from reused import arguments, read_file
import sys

PATH="2020/day12/input.txt"
DIRECTIONS = ["N","E","S","W"]
ACTIONS = ["F","L","R"]

class FerryBoat:
  def __init__(self):
    self.dir = 1
    self.pos_x = 0
    self.pos_y = 0

  def __repr__(self):
    return '<FerryBoat(Facing={self.dir!r}) (POS=({self.pos_y!r},{self.pos_x!r}))>'.format(self=self)
  
  def parse_instruction(self,instruction):
    dir = instruction[0]
    val = instruction[1:]

    try:
      val = int(val)
    except ValueError:
      print("Error in instructions, value not integer")
      sys.exit()

    if (dir in ACTIONS):
      if (dir == ACTIONS[0]):
        self.move_forward(val)
      elif (dir == ACTIONS[1]):
        self.turn_left(val)
      elif (dir == ACTIONS[2]):
        self.turn_right(val)
    elif (dir in DIRECTIONS):
      if (dir == DIRECTIONS[0]):
        self.pos_y += val
      elif (dir == DIRECTIONS[1]):
        self.pos_x += val
      elif (dir == DIRECTIONS[2]):
        self.pos_y -= val
      elif (dir == DIRECTIONS[3]):
        self.pos_x -= val

  def move_forward(self,val):
    if (DIRECTIONS[self.dir] == DIRECTIONS[0]):
      self.pos_y += val
    elif (DIRECTIONS[self.dir] == DIRECTIONS[1]):
      self.pos_x += val
    elif (DIRECTIONS[self.dir] == DIRECTIONS[2]):
      self.pos_y -= val
    elif (DIRECTIONS[self.dir] == DIRECTIONS[3]):
      self.pos_x -= val

  def turn_left(self,val):
    steps = int(val / 90)
    self.dir -= steps
    while (self.dir < 0):
      self.dir += len(DIRECTIONS)

  def turn_right(self,val):
    steps = int(val / 90)
    self.dir += steps
    while (self.dir >= len(DIRECTIONS)):
      self.dir -= len(DIRECTIONS)

  def calc_distance(self):
    return abs(self.pos_x) + abs(self.pos_y)

def part1(path):
  navigation_instructions = read_file(path or PATH,return_type=str,strip=True)
  
  ferry_boat = FerryBoat()
  for instruction in navigation_instructions:
    ferry_boat.parse_instruction(instruction)

  print(ferry_boat.calc_distance())

class WaypointBoat():
  def __init__(self):
    self.dir = 1
    self.pos_x = 0
    self.pos_y = 0
    self.way_x = 10
    self.way_y = 1

  def __str__(self):
    return """ WaypointBoat:
      Facing: """ + DIRECTIONS[self.dir] + """
      POS: {
        x: """ + str(self.pos_x) + """
        y: """ + str(self.pos_y) + """
      }
      Waypoint: {
        x: """ + str(self.way_x) + """
        y: """ + str(self.way_y) + """
      }"""

  def parse_instruction(self,instruction):
    dir = instruction[0]
    val = instruction[1:]

    # print(instruction)

    try:
      val = int(val)
    except ValueError:
      print("Error in instructions, value not integer")
      sys.exit()

    if (dir in ACTIONS):
      if (dir == ACTIONS[0]):
        self.move_forward(val)
      elif (dir == ACTIONS[1]):
        for i in range(int(val/90)):
          self.turn_left(val)
      elif (dir == ACTIONS[2]):
        for i in range(int(val/90)):
          self.turn_right(val)
    elif (dir in DIRECTIONS):
      if (dir == DIRECTIONS[0]):
        self.way_y += val
      elif (dir == DIRECTIONS[1]):
        self.way_x += val
      elif (dir == DIRECTIONS[2]):
        self.way_y -= val
      elif (dir == DIRECTIONS[3]):
        self.way_x -= val
  
  def move_forward(self,val):
      self.pos_x += self.way_x * val
      self.pos_y += self.way_y * val

  def turn_left(self,val):
    temp = self.way_y * -1
    self.way_y = self.way_x
    self.way_x = temp

  def turn_right(self,val):
    temp = self.way_x * -1
    self.way_x = self.way_y
    self.way_y = temp
    pass

  def calc_distance(self):
    return abs(self.pos_x) + abs(self.pos_y)

  

def part2(path):
  navigation_instructions = read_file(path or PATH,return_type=str,strip=True)
  
  waypoint_boat = WaypointBoat()
  for instruction in navigation_instructions:
    waypoint_boat.parse_instruction(instruction)
    # print(waypoint_boat)

  print(waypoint_boat.calc_distance())

if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")