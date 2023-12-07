from common.binaryTree import BinaryTree, BinaryTreeNode

class AVLTree(BinaryTree):

    def display(self):
        print("Hello")
        
#   def insert(self,data):
#       if self.root==None:
#           self.root=Node(data)

#       else:
#         current=self.root
#         while 1:
#             if data < current.data:
#                 if current.left:
#                     current=current.left
#                 else:
#                     current.left=Node(data)
#                     break
#             elif data > current.data:
#                 if current.right:
#                     current=current.right
#                 else:
#                     current.right=Node(data)
#                     break
#             else:
#                 break