from reused import arguments, read_file

PATH = "2021/day05/input.txt"

class Grid:
  def __init__(self):
    self.board = []

  def count_overlap(self):
    overlap = 0
    for row in self.board:
      for col in row:
        if (col >= 2):
          overlap += 1
    return overlap

  def add_vert(self,start,end):
    inc = 1 if start[1] <= end[1] else -1
    for row in range(start[1],end[1]+inc,inc):
      self.board[row][start[0]] += 1

  def add_horz(self,start,end):
    inc = 1 if start[0] <= end[0] else -1
    for x in range(start[0],end[0]+inc,inc):
      self.board[start[1]][x] += 1

  def add_diag(self,start,end,left,up):
    magnitude = abs(start[0] - end[0])
    inc_w = -1 if left else 1
    inc_h = -1 if up else 1
    for i in range(magnitude+1):
      self.board[start[1]+(inc_h*i)][start[0]+(inc_w*i)] += 1


  def add_line(self,start,end,diagonal):
    if (start[0] == end[0]):
      self.add_vert(start,end)
    if (start[1] == end[1]):
      self.add_horz(start,end)
    if (diagonal):
      if (start[0] > end[0] and start[1] > end[1]):
        self.add_diag(start,end,True,True)
      if (start[0] < end[0] and start[1] > end[1]):
        self.add_diag(start,end,False,True)
      if (start[0] > end[0] and start[1] < end[1]):
        self.add_diag(start,end,True,False)
      if (start[0] < end[0] and start[1] < end[1]):
        self.add_diag(start,end,False,False)

  def make_board(self,pairs):
    longest_val = 0
    highest_val = 0

    for start,end in pairs:
      if start[0] > longest_val:
        longest_val = start[0]
      if end[0] > longest_val:
        longest_val = end[0]
      if start[1] > highest_val:
        highest_val = start[1]
      if end[1] > highest_val:
        highest_val = end[1]

    for i in range(highest_val+1):
      row = [0]*(longest_val+1)
      self.board.append(row)

  def display(self):
    for row in self.board:
      for col in row:
        if (col == 0):
          print('.', end=" ")
        else:
          print(col, end=" ")
      print()
    

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  grid = Grid()
  
  pairs = []
  for line in file_data:
    start,end = line.split('->')
    start = [int(x) for x in start.split(",")]
    end = [int(x) for x in end.split(",")]
    pairs.append((start,end))
  grid.make_board(pairs)

  for start,end in pairs:
    grid.add_line(start,end)

  return(grid.count_overlap())
      

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  grid = Grid()
  
  pairs = []
  for line in file_data:
    start,end = line.split('->')
    start = [int(x) for x in start.split(",")]
    end = [int(x) for x in end.split(",")]
    pairs.append((start,end))
  grid.make_board(pairs)

  for start,end in pairs:
    grid.add_line(start,end,True)

  return(grid.count_overlap())


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")