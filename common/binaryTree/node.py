class BinaryTreeNode:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data
        self.duplicates = []