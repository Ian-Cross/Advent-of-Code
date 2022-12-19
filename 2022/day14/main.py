from reused import arguments, read_file
from operator import add

PATH = "2022/day14/test.txt"


def get_cave_size(segments):
    max_x, max_y = 0, 0
    for segment in segments:
        for point in segment:
            if point[0] > max_x:
                max_x = point[0]
            if point[1] > max_y:
                max_y = point[1]
    return max_y, max_x


def print_board(board):
    for y, _ in enumerate(board):
        for x, _ in enumerate(board[y]):
            if 450 < x < 550:
                print(board[y][x], end='')
        print()


def draw_rocks(segments, board):
    for segment in segments:
        segment.sort()
        for x in range(segment[0][0], segment[1][0]+1):
            for y in range(segment[0][1], segment[1][1]+1):
                board[y][x] = '#'


def move_sand(sand, board, bottom):
    if sand[0]+1 == bottom:
        return False, sand

    board[sand[0]][sand[1]] = '.'

    if board[sand[0]+1][sand[1]] == '.':
        sand = list(map(add, sand, [1, 0]))

    elif board[sand[0]+1][sand[1]-1] == '.':
        sand = list(map(add, sand, [1, -1]))

    elif board[sand[0]+1][sand[1]+1] == '.':
        sand = list(map(add, sand, [1, 1]))

    else:
        board[sand[0]][sand[1]] = 'o'
        return True, sand

    return move_sand(sand, board, bottom)


def part1(path):
    file_data = read_file(path or PATH, return_type=str,
                          strip=True, split="->")

    segments = []
    for line in file_data:
        for idx, _ in enumerate(line[:-1]):
            segments.append([tuple([int(x) for x in line[idx].split(",")]),
                            tuple([int(x) for x in line[idx+1].split(",")])])

    max_y, max_x = get_cave_size(segments)
    board = [['.' for _ in range(max_x+1)] for _ in range(max_y+1)]

    draw_rocks(segments, board)

    sand_count = 0
    while True:
        did_rest, rest_pos = move_sand([0, 500], board, len(board))
        if did_rest:
            sand_count += 1
        else:
            break

    return sand_count


def part2(path):
    file_data = read_file(path or PATH, return_type=str,
                          strip=True, split="->")

    segments = []
    for line in file_data:
        for idx, _ in enumerate(line[:-1]):
            segments.append([tuple([int(x) for x in line[idx].split(",")]),
                            tuple([int(x) for x in line[idx+1].split(",")])])

    max_y, max_x = get_cave_size(segments)

    board = [['.' for _ in range(max_x*2)] for _ in range(max_y+2)]
    board.append(['#' for _ in range(max_x*2)])

    draw_rocks(segments, board)

    sand_count = 0
    while True:
        did_rest, rest_pos = move_sand([0, 500], board, len(board)+1)
        if did_rest:
            sand_count += 1
            if rest_pos == [0, 500]:
                break
        else:
            break
    return sand_count


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
