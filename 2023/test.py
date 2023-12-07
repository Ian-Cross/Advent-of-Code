from common.avlTree import AVLTree
from common.binaryTree import BinaryTree
import random


def main():
  
  # avl_tree = AVLTree()
  binary_tree = BinaryTree()

  find_me = 0
  for i,_ in enumerate(range(50)):
    temp = random.randint(0,100)
    if i == 20:
      find_me = temp

    # avl_tree.insert(temp)

    binary_tree.insert(temp)
    for _ in range(random.randint(0,4)):
      binary_tree.insert(temp)

  binary_tree.display()
  node = binary_tree.search(find_me)

  if node == None:
    print("Node not found")
  else:
    print(f" Found you: {node.data}")



  for _ in range(len(node.duplicates)+1):
    binary_tree.delete(node)
    binary_tree.display()



if __name__ == "__main__":
  main()