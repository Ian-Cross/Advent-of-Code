from reused import arguments, read_file
from common.grid import Grid
from collections import deque
from common.constants import CARDINAL_NEIGHBOURS

PATH = "2025/day09/test.txt"

FULL = "#"
EMPTY = "."

def query_psm(psm: list[list[int]], x1, y1, x2, y2) -> int:
    total = psm[x2][y2]
    left = psm[x1-1][y2] if x1 > 0 else 0
    top = psm[x2][y1-1] if y1 > 0 else 0
    topleft = psm[x1-1][y1-1] if x1 > 0 < y1 else 0
    return total - left - top + topleft

def psm(fn,grid: Grid) -> list[list[int]]:
    '''
    Creates a prefix sums matrix for the given grid based on the function fn
    '''
    psm = [[0] * grid.width for _ in range(grid.height)]
    for x in range(grid.width):
        for y in range(grid.height):
            left = psm[x-1][y] if x > 0 else 0
            top = psm[x][y-1] if y > 0 else 0
            topleft = psm[x-1][y-1] if x > 0 < y else 0
            psm[x][y] = left + top - topleft + fn(x, y)
    return psm

def compressed_coords(x1, y1, x2, y2, xs, ys):
    cx1,cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
    cy1,cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])
    return ((cx1,cy1),(cx2,cy2))

def area(x1, y1, x2, y2):
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
    return (max_x - min_x + 1) * (max_y - min_y + 1)

def part1(path):
    file_data = read_file(path or PATH, return_type=int, strip=True, split=",")

    rectangles = [0]
    for i in range(0, len(file_data)):
        for j in range(i, len(file_data)):
            a, b = file_data[i], file_data[j]
            rectangles.append(area(*a, *b))

    return max(rectangles)


def part2(path):
    file_data = read_file(path or PATH, return_type=int, strip=True, split=",")
    grid = Grid()

    xs = sorted({x for x, _ in file_data})
    ys = sorted({y for _, y in file_data})

    grid.fill([[EMPTY] * (len(ys) * 2 - 1) for _ in range(len(xs) * 2 - 1)])

    for p1,p2 in zip(file_data, file_data[1:] + file_data[:1]):
        c1, c2 = compressed_coords(*p1, *p2, xs, ys)

        for cy in range(c1[0], c2[0] + 1):
            for cx in range(c1[1], c2[1] + 1):
                grid.set((cx, cy), FULL)

    # Flood fill the outside of the grid to determin what is inside
    outside = {(-1, -1)}
    queue = deque(outside)
    while queue:
        pos = queue.popleft()
        for n in CARDINAL_NEIGHBOURS:
            # allowing 1 block outside to ensure the flood gets around the edges
            if (not grid.in_bounds(pos, n, buffer=1)):
                continue
            if grid.in_bounds(pos,n) and grid.get(pos,n) == FULL:  # We found a wall
                continue
            new_pos = tuple(map(lambda i,j: i+j,pos,n))
            if new_pos in outside:
                continue
            outside.add(new_pos)
            queue.append(new_pos)

    grid.traverse(lambda _,row_num,__,col_num: grid.set((col_num,row_num), FULL) if (col_num,row_num) not in outside else None)
    # grid.display(delim='', line_break='\n')
    
    grid.calculate_psm(lambda y,x: 1 if grid.get((y,x)) == FULL else 0)
    pairs = [(p1,p2) for i,p1 in enumerate(file_data) for j,p2 in enumerate(file_data) if i != j]

    rectangles = []
    for p1,p2 in pairs:
        c1,c2 = compressed_coords(*p1, *p2, xs, ys)
        if grid.query_psm(*c1,*c2) == area(*c1, *c2):
            rectangles.append(area(*p1, *p2))
    return max(rectangles)

if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
