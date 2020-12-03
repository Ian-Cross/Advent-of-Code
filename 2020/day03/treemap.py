from reused import arguments, read_file
import math

PATH="2020/day03/input.txt"
TREE="#"

def take_step(position,slope):
  return [position[0]+slope[0],position[1]+slope[1]]

def walk_slope(tree_rows,position,slope,max_height,max_width):
  tree_count = 0
  while position[0] < max_height:
    position = take_step(position,slope)
    if position[1] >= max_width:
      position[1] -= max_width +1
    if (tree_rows[position[0]][position[1]] == TREE):
      tree_count += 1
  return tree_count

def part1(path):
  tree_rows = read_file(path or PATH,return_type=str,strip=True)
  position = [0,0]
  max_width = len(tree_rows[0])-1
  max_height = len(tree_rows)-1
  slope = [1,3]

  tree_count = walk_slope(tree_rows,position,slope,max_height,max_width)

  print(tree_count)


def part2(path):
  tree_rows = read_file(path or PATH,return_type=str,strip=True)
  slopes = [[1,1],[1,3],[1,5],[1,7],[2,1]]
  max_width = len(tree_rows[0])-1
  max_height = len(tree_rows)-1
  tree_counts = []

  for slope in slopes:
    position = [0,0]
    tree_count = walk_slope(tree_rows,position,slope,max_height,max_width)
    tree_counts.append(tree_count)

  print(math.prod(tree_counts))

if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")