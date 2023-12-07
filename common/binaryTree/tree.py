from .node import BinaryTreeNode

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root==None:
            self.root=BinaryTreeNode(data)

        else:
            current=self.root
            while 1:
                if data < current.data:
                    if current.left:
                        current=current.left
                    else:
                        current.left=BinaryTreeNode(data)
                        break
                elif data > current.data:
                    if current.right:
                        current=current.right
                    else:
                        current.right=BinaryTreeNode(data)
                        break
                else:
                    current.duplicates.append(BinaryTreeNode(data))
                    break
    

    def search(self, key) -> BinaryTreeNode:
        return self._left_weighted_depth_search(self.root, key)

    def _left_weighted_depth_search(self, node, key) -> BinaryTreeNode:
        if node.data == key:
            return node
      
        if node.left:
            curr = self._left_weighted_depth_search(node.left, key)
            if curr is not None:
                return curr

        if node.right:
            curr = self._left_weighted_depth_search(node.right, key)
            if curr is not None:
                return curr
            
        return None
    
    def _right_weighted_depth_search(self, node, key) -> BinaryTreeNode:
        if node.data == key:
            return node
      
        if node.left:
            curr = self._right_weighted_depth_search(node.left, key)
            if curr is not None:
                return curr

        if node.right:
            curr = self._right_weighted_depth_search(node.right, key)
            if curr is not None:
                return curr
            
        return None

    def delete(self, node):
        node = self.search(node.data)
        if node == None:
            return False

        if len(node.duplicates) > 0:
            node.duplicates.pop(0)
            return True
        
        deepNode = self.find_deep_node(self.root)
        print(deepNode.data)
        node.data = deepNode.data
        node.duplicates = deepNode.duplicates

        self.delete_deepest(self.root,deepNode)


    def find_deep_node(self,node):
        if node.left:
            return self.find_deep_node(node.left)
        if node.right:
            return self.find_deep_node(node.right)
        return node
    
    def delete_deepest(self,curr, target):
        if curr.left:
            if curr.left is target:
                curr.left = None
                return
            else:
                return self.delete_deepest(curr.left,target)

        if curr.right:
            if curr.right is target:
                curr.right = None
                return
            else:
                return self.delete_deepest(curr.right,target)


    def display(self):
        lines, *_ = self._display(self.root)
        for line in lines:
            print(line)

    def _display(self, current):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
      
        # No child.
        if current.right is None and current.left is None:
            line = f"{current.data}:{len(current.duplicates)}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

      # Only left child.
        if current.right is None:
            lines, n, p, x = self._display(current.left)
            s = f"{current.data}:{len(current.duplicates)}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if current.left is None:
            lines, n, p, x = self._display(current.right)
            s = f"{current.data}:{len(current.duplicates)}"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display(current.left)
        right, m, q, y = self._display(current.right)
        s = f"{current.data}:{len(current.duplicates)}"
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