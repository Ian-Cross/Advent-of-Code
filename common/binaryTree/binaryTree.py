from .node import Node

class Tree:
  def __init__(self):
    self.root = None

  def insert(self,data):
      if self.root==None:
          self.root=Node(data)

      else:
        current=self.root
        while 1:
            if data < current.data:
                if current.left:
                    current=current.left
                else:
                    current.left=Node(data)
                    break
            elif data > current.data:
                if current.right:
                    current=current.right
                else:
                    current.right=Node(data)
                    break
            else:
                break
            

  def display(self):
      lines, *_ = self._display(self.root)
      for line in lines:
          print(line)

  def _display(self, current):
      """Returns list of strings, width, height, and horizontal coordinate of the root."""
      
      # No child.
      if current.right is None and current.left is None:
          line = '%s' % current.data
          width = len(line)
          height = 1
          middle = width // 2
          return [line], width, height, middle

      # Only left child.
      if current.right is None:
          lines, n, p, x = self._display(current.left)
          s = '%s' % current.data
          u = len(s)
          first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
          second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
          shifted_lines = [line + u * ' ' for line in lines]
          return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

      # Only right child.
      if current.left is None:
          lines, n, p, x = self._display(current.right)
          s = '%s' % current.data
          u = len(s)
          first_line = s + x * '_' + (n - x) * ' '
          second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
          shifted_lines = [u * ' ' + line for line in lines]
          return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

      # Two children.
      left, n, p, x = self._display(current.left)
      right, m, q, y = self._display(current.right)
      s = '%s' % current.data
      u = len(s)
      first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
      second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
      if p < q:
          left += [n * ' '] * (q - p)
      elif q < p:
          right += [m * ' '] * (p - q)
      zipped_lines = zip(left, right)
      lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
      return lines, n + m + u, max(p, q) + 2, n + u // 2