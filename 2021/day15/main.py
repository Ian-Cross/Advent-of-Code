from reused import arguments, read_file
from math import floor

PATH = "2021/day15/test.txt"


class Node():
    def __init__(self, risk, cummulative_risk, row, col):
        self.risk = risk
        self.cummulative_risk = cummulative_risk + risk
        self.row = row
        self.col = col
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.add_parent(self)

    def add_parent(self, parent):
        self.parent = parent

    def __eq__(self, object):
        if not isinstance(object, Node):
            return False

        if object.risk != self.risk:
            return False

        if object.row != self.row:
            return False

        if object.col != self.col:
            return False

        return True

    def __repr__(self):
        return f"< Node risk: {self.risk} at ({self.row},{self.col}) >"


def display_grid(grid):
    for row in grid:
        for col in row:
            print(col, end=" ")
        print()


def in_bounds(grid, row, col):
    if (row < 0 or col < 0):
        return False
    if (row >= len(grid) or col >= len(grid[row])):
        return False
    return True


# Up, left, down, right
ADJ = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def get_neighbours(grid, cn):
    neighbours = []
    for c, r in ADJ:
        if in_bounds(grid, cn.row+r, cn.col+c):
            neighbours.append(
                Node(grid[cn.row+r][cn.col+c], cn.cummulative_risk, cn.row+r, cn.col+c))
    return neighbours


def is_bottom(node, grid):
    return node.row == len(grid)-1 and node.col == len(grid[node.row])-1


def insert_child(arr, node):
    if len(arr) == 0:
        return [node]

    new_arr = []
    flag = False
    for el in arr:
        if not flag and el.cummulative_risk > node.cummulative_risk:
            new_arr.append(node)
            flag = True
        new_arr.append(el)
    if not flag:
        new_arr.append(node)

    return new_arr


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    grid = []
    for row in file_data:
        grid_row = []
        for col in row:
            grid_row.append(int(col))
        grid.append(grid_row)

    curr_node = Node(grid[0][0], -grid[0][0], 0, 0)
    already_looked_at = [curr_node]
    child_privaliage = [curr_node]

    while len(child_privaliage) > 0:
        # pick next target off of priority queue
        curr_node = child_privaliage[0]
        child_privaliage = child_privaliage[1:]

        if is_bottom(curr_node, grid):
            break

        # retrieve all their children
        neighbours = get_neighbours(grid, curr_node)

        for neighbour in neighbours:
            if neighbour not in already_looked_at:
                # add to node
                curr_node.add_child(neighbour)
                # don't look at this neighbour again
                already_looked_at.append(neighbour)
                # add children onto priority queue
                child_privaliage = insert_child(child_privaliage, neighbour)

    return curr_node.cummulative_risk


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    grid = []
    for row in file_data:
        grid_row = []
        for col in row:
            grid_row.append(int(col))
        grid.append(grid_row)

    bigger_grid = []
    height = len(grid)
    width = len(grid[0])
    for i in range(height*5):
        bigger_row = []
        for j in range(width*5):
            val = (grid[i % height][j % width] +
                   floor(j/width) + floor(i/height))
            if (val > 9):
                val = val % 9
            bigger_row.append(val)
        bigger_grid.append(bigger_row)

    grid = bigger_grid

    curr_node = Node(bigger_grid[0][0], -bigger_grid[0][0], 0, 0)
    already_looked_at = [curr_node]
    child_privaliage = [curr_node]

    while len(child_privaliage) > 0:
        # pick next target off of priority queue
        curr_node = child_privaliage[0]
        # print(f"Curr Node {curr_node}")
        child_privaliage = child_privaliage[1:]

        if is_bottom(curr_node, grid):
            break

        # retrieve all their children
        neighbours = get_neighbours(bigger_grid, curr_node)

        for neighbour in neighbours:
            # print(f"Neighbour: {neighbour}", end = "")
            if neighbour not in already_looked_at:
                # print(' - NEW')
                # add to node
                curr_node.add_child(neighbour)
                already_looked_at.append(neighbour)
                # add children onto priority queue
                child_privaliage = insert_child(child_privaliage, neighbour)
                # print("Privalage List")
                # print(child_privaliage)
            # else:
                # print(' - SEEN')

        # input()

    # sum = 0
    # print(curr_node.cummulative_risk)
    # while curr_node.row != 0 or curr_node.col != 0:
    #   sum += int(curr_node.risk)
    #   print(curr_node)
    #   curr_node = curr_node.parent
    # sum += int(curr_node.risk)
    # print(curr_node)
    # curr_node = curr_node.parent
    return curr_node.cummulative_risk


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
