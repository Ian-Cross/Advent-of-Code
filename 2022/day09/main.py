from reused import arguments, read_file
import operator
import math

PATH = "2022/day09/test.txt"

directions = {
    'R': (0, 1),
    'RD': (-1, 1),
    'D': (-1, 0),
    'LD': (-1, -1),
    'L': (0, -1),
    'LU': (1, -1),
    'U': (1, 0),
    'RU': (1, 1),
    'S': (0, 0)
}


def in_view(H, T):
    for dir in directions:
        visibile = tuple(map(operator.add, T, directions[dir]))
        if H == visibile:
            return True
    return False


def calc_adjustment(H, T):
    vert_move, horz_move = 0, 0

    if H[0]-T[0] == 2:
        vert_move = 1
        if H[1]-T[1] < 0:
            horz_move = -1
        elif H[1]-T[1] > 0:
            horz_move = 1
    elif H[0]-T[0] == -2:
        vert_move = -1
        if H[1]-T[1] < 0:
            horz_move = -1
        elif H[1]-T[1] > 0:
            horz_move = 1

    elif H[1]-T[1] == 2:
        horz_move = 1
        if H[0]-T[0] < 0:
            vert_move = -1
        elif H[0]-T[0] > 0:
            vert_move = 1
    elif H[1]-T[1] == -2:
        horz_move = -1
        if H[0]-T[0] < 0:
            vert_move = -1
        elif H[0]-T[0] > 0:
            vert_move = 1

    return (vert_move, horz_move)


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    positions = []
    T = (0, 0)
    H = (0, 0)

    for line in file_data:
        dir, steps = line.split()

        for _ in range(int(steps)):
            H = tuple(map(operator.add, H, directions[dir]))
            T = tuple(map(operator.add, T, calc_adjustment(H, T)))
            positions.append(T)
    return (len(set(positions)))


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    positions = []
    rope = [(0, 0)]*10

    for line in file_data:
        dir, steps = line.split()
        for _ in range(int(steps)):

            rope[0] = tuple(map(operator.add, rope[0], directions[dir]))
            for segment in range(1, len(rope)):
                rope[segment] = tuple(map(operator.add, rope[segment], calc_adjustment(
                    rope[segment-1], rope[segment])))
                if segment == len(rope)-1:
                    positions.append(rope[segment])

    return (len(set(positions)))


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
