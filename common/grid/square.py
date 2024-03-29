

class Square:
  def __init__(self,data):
    self.data = data

  def display(self,delim='\n'):
    print(self.data,end=delim)

  def __eq__(self,other):
    if not isinstance(other,Square):
      return NotImplemented
    
    return self.data == other.data