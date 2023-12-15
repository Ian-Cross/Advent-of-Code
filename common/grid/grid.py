from .square import Square

class Grid:
  def __init__(self):
    self.matrix = None
    self.height = None
    self.width = None

  def display(self,delim='\n', line_break = None) -> None:
    for y, row in enumerate(self.matrix):
      for x, col in enumerate(row):
        col.display(delim)
      if (line_break): 
        print()

  def fill(self, grid, height = None, width = None) -> None:
    matrix = []
    max_width = 0
    for y,line in enumerate(grid):
      row = []
      for x,el in enumerate(line):
        row.append(Square(el))

      if len(row) > max_width:
        max_width = len(row)

      matrix.append(row)
    self.height = len(matrix)
    self.width = max_width
    self.matrix = matrix

  def traverse(self,callback = lambda row,row_num,col,col_num: None) -> None:
    for y, row in enumerate(self.matrix):
      for x, col in enumerate(row):
        callback(row,y,col,x)

  def insert_row(self,row,idx):
    
    if len(row) != self.width:
      return -1
    
    self.height += 1
    self.matrix.insert(idx,row)
  
  def insert_column(self,col,idx):

    if len(col) != self.height:
      return -1

    self.width += 1
    for row_num, row in enumerate(self.matrix):
      row.insert(idx,col[row_num])

  def in_bounds(self,pos: tuple[int,int],n: tuple[int,int] = None) -> bool:
    new_pos = pos
    if n is not None:
      new_pos = tuple(map(lambda i,j: i+j,pos,n))

    if new_pos[1] >= self.width or new_pos[1] < 0:
      return False
    if new_pos[0] >= self.height or new_pos[0] < 0:
      return False
    return True
  
  def at(self,pos: tuple[int,int]) -> Square:
    return self.matrix[pos[0]][pos[1]]
  
  def set(self,pos: tuple[int,int],value) -> None:
    self.matrix[pos[0]][pos[1]].data = value
  
  def rotate_90(self,clockwise = True):
    self.matrix = list(zip(*self.matrix[::-1]))