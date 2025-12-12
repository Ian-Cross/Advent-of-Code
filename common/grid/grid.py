from .square import Square

class Grid:
  def __init__(self):
    self.matrix = None
    self.height = None
    self.width = None
    self.psm = None

  def display(self,delim='\n', line_break = None) -> None:
    for y, row in enumerate(self.matrix):
      for x, col in enumerate(row):
        col.display(delim)
      if (line_break): 
        print()

  def fill(self, grid, height = None, width = None, callback = None) -> None:
    matrix = []
    max_width = 0
    for y,line in enumerate(grid):
      row = []
      for x,el in enumerate(line):
        row.append(Square(el))
        if callback:
          callback(row,y,row[-1],x)

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

  def in_bounds(self,pos: tuple[int,int],n: tuple[int,int] = None, buffer: int = 0) -> bool:
    new_pos = pos
    if n is not None:
      new_pos = tuple(map(lambda i,j: i+j,pos,n))

    if new_pos[1] >= (self.width + buffer) or new_pos[1] < (0 - buffer):
      return False
    if new_pos[0] >= (self.height + buffer) or new_pos[0] < (0 - buffer):
      return False
    return True
  
  def at(self,pos: tuple[int,int], n: tuple[int,int] = None) -> Square:
    new_pos = pos
    if n is not None:
      new_pos = tuple(map(lambda i,j: i+j,pos,n))
    return self.matrix[new_pos[0]][new_pos[1]]

  def get(self,pos: tuple[int,int],n: tuple[int,int] = None):
    new_pos = pos
    if n is not None:
      new_pos = tuple(map(lambda i,j: i+j,pos,n))
    return self.matrix[new_pos[0]][new_pos[1]].data

  def set(self,pos: tuple[int,int],value, n: tuple[int,int] = None) -> None:
    new_pos = pos
    if n is not None:
      new_pos = tuple(map(lambda i,j: i+j,pos,n))
    self.matrix[new_pos[0]][new_pos[1]].data = value

  def rotate_90(self,clockwise = True):
    self.matrix = list(zip(*self.matrix[::-1]))

  def size(self):
    return (self.height,self.width)
  
  def count(self):
    return self.height * self.width
  
  def row(self,idx: int) -> list[Square]:
    return self.matrix[idx]

  def calculate_psm(self,fn):
    psm = [[0] * self.width for _ in range(self.height)]
    for y in range(self.width):
      for x in range(self.height):
        left = psm[y][x-1] if x > 0 else 0
        top = psm[y-1][x] if y > 0 else 0
        topleft = psm[y-1][x-1] if y > 0 < x else 0
        psm[y][x] = left + top - topleft + fn(x,y)
    self.psm = psm

  def query_psm(self, x1, y1, x2, y2):
    if self.psm is None:
      raise ValueError("Prefix Sum Matrix not computed.")
    total = self.psm[x2][y2]
    left = self.psm[x1-1][y2] if x1 > 0 else 0
    top = self.psm[x2][y1-1] if y1 > 0 else 0
    topleft = self.psm[x1-1][y1-1] if x1 > 0 < y1 else 0
    return total - left - top + topleft