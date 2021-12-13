from reused import arguments, read_file
from math import floor

PATH = "2021/day13/input.txt"


def add_point(x, y, grid):
    if y >= len(grid):
        for _ in range(y-len(grid) + 1):
            grid.append(["_"]*(x+1))

    for row in grid:
        if x >= len(row):
            for _ in range(x - len(row) + 1):
                row.append("_")
    grid[y][x] = "."
    return grid


def fold_y(grid, level):
    new_grid = []
    if (level % 2 == 0):
      for y in range(floor(len(grid)/2)+1):
          row = []
          for (a, b) in zip(grid[y], grid[len(grid)-y-1]):
              row.append(a if a == "." else b)
          new_grid.append(row)
    else:
      for y in range(floor(len(grid)/2)):
          row = []
          for (a, b) in zip(grid[y], grid[len(grid)-y-1]):
              row.append(a if a == "." else b)
          new_grid.append(row)
    return new_grid


def fold_x(grid, level):
    new_grid = []
    if (level % 2 == 0):
      for y in grid:
          new_row = []
          for x in range(floor(len(y)/2) + 1):
              new_row.append(y[x] if y[x] == "." else y[len(y)-x-1])
          new_grid.append(new_row)
    else:
      for y in grid:
          new_row = []
          for x in range(floor(len(y)/2)):
              new_row.append(y[x] if y[x] == "." else y[len(y)-x-1])
          new_grid.append(new_row)
    return new_grid


def display_grid(grid):
    for row, _ in enumerate(grid):
        for col, _ in enumerate(grid[row]):
            print(grid[row][col], end="")
        print()


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    grid = []
    for point in file_data:
        if point == "":
            break
        x, y = point.split(",")
        grid = add_point(int(x), int(y), grid)

    folds = []
    f = False
    for fold in file_data:
        if f:
            folds.append(fold.split(' ')[2])
        if fold == "":
            f = True


    for fold in folds:
        [dir, line] = fold.split('=')
        if (dir == "y"):
            grid = fold_y(grid, int(line))
        if (dir == "x"):
            grid = fold_x(grid, int(line))
        break

    count = 0
    for row, _ in enumerate(grid):
        for col, _ in enumerate(grid[row]):
            if grid[row][col] == ".":
                count += 1
    return count


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    
    grid = []
    for point in file_data:
        if point == "":
            break
        x, y = point.split(",")
        grid = add_point(int(x), int(y), grid)

    folds = []
    f = False
    for fold in file_data:
        if f:
            folds.append(fold.split(' ')[2])
        if fold == "":
            f = True


    for fold in folds:
        [dir, line] = fold.split('=')
        if (dir == "y"):
            grid = fold_y(grid, int(line))
        if (dir == "x"):
            grid = fold_x(grid, int(line))
    display_grid(grid)


if __name__ == "__main__":
    print(arguments(part1, part2))
    print("\n")
