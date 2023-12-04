from reused import arguments, read_file
from functools import reduce
import operator
import re
from common.grid import Grid, Square
from common.constants import NEIGHBOURS

PATH = "2023/day03/input.txt"

symbols = set[tuple[int, int]]()


def is_star(row: list[Square], row_num: int, col: Square, col_num: int):
    global symbols
    if col.data == "*":
        symbols.add((row_num, col_num))

def is_symbol(row: list[Square], row_num: int, col: Square, col_num: int):
    global symbols
    if re.match("\@|\#|\$|\%|\&|\*|/|\+|\=|\-",col.data):
        symbols.add((row_num, col_num))


def part1(path):
    global symbols
    file_data = read_file(path or PATH, return_type=str, strip=True)

    grid = Grid()
    grid.fill(file_data)
    # grid.display(delim="", line_break=True)

    grid.traverse(is_symbol)

    sum = 0
    for s in symbols:
        for n in NEIGHBOURS:
            if not grid.in_bounds(s, n):
                continue

            (y, x) = tuple[int, int](map(lambda i, j: i + j, s, n))
            num = grid.at((y, x)).data

            if not num.isnumeric():
                continue

            grid.set((y,x),'.')

            p = x-1
            while p >= 0 and grid.at((y,p)).data.isnumeric():
                num = grid.at((y,p)).data + num
                grid.set((y,p),'.')
                p-=1

            p = x+1
            while p < grid.width and grid.at((y,p)).data.isnumeric():
                num += grid.at((y,p)).data
                grid.set((y,p),'.')
                p+=1

            sum += int(num)
    return sum


def part2(path):
    global symbols
    file_data = read_file(path or PATH, return_type=str, strip=True)

    grid = Grid()
    grid.fill(file_data)
    # grid.display(delim="", line_break=True)

    grid.traverse(is_star)

    ratios = 0
    for s in symbols:
        nums = []
        for n in NEIGHBOURS:
            if not grid.in_bounds(s, n):
                continue

            (y, x) = tuple[int, int](map(lambda i, j: i + j, s, n))
            num = grid.at((y,x)).data

            if not num.isnumeric():
                continue

            grid.set((y,x),".")

            p = x - 1
            while p >= 0 and grid.at((y,p)).data.isnumeric():
                num = grid.at((y,p)).data + num
                grid.set((y,p),".")
                p -= 1

            p = x + 1
            while p < grid.width and grid.at((y,p)).data.isnumeric():
                num += grid.at((y,p)).data
                grid.set((y,p),".")
                p += 1

            nums.append(int(num))

        if len(nums) > 1:
            ratios += reduce(operator.mul, nums, 1)

    return ratios


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
