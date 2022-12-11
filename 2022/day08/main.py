from reused import arguments, read_file

PATH = "2022/day08/test.txt"


def is_visible_up(forrest, tree, x, y):
    for _y in range(y-1, -1, -1):
        if tree <= forrest[_y][x]:
            return False
    return True


def is_visible_down(forrest, tree, x, y, size):
    for _y in range(y+1, size, 1):
        if tree <= forrest[_y][x]:
            return False
    return True


def is_visible_left(forrest, tree, x, y):
    for _x in range(x-1, -1, -1):
        if tree <= forrest[y][_x]:
            return False
    return True


def is_visible_right(forrest, tree, x, y, size):
    for _x in range(x+1, size, 1):
        if tree <= forrest[y][_x]:
            return False
    return True


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    forrest = []

    for line in file_data:
        tree_line = []
        for x in line:
            tree_line.append(int(x))
        forrest.append(tree_line)

    size = len(forrest[0])
    inner_visible_count = 0
    outer_visible_count = 0
    for y, tree_line in enumerate(forrest):
        for x, tree in enumerate(tree_line):
            if x == 0 or x == size-1 or y == 0 or y == size-1:
                outer_visible_count += 1
                continue

            if is_visible_up(forrest, tree, x, y):
                # print(f"\t visible up")
                inner_visible_count += 1
                continue

            if is_visible_right(forrest, tree, x, y, size):
                # print(f"\t visible right")
                inner_visible_count += 1
                continue

            if is_visible_left(forrest, tree, x, y):
                # print(f"\t visible left")
                inner_visible_count += 1
                continue

            if is_visible_down(forrest, tree, x, y, size):
                # print(f"\t visible down")
                inner_visible_count += 1
                continue

    return inner_visible_count+outer_visible_count


def scenic_score_up(forrest, tree, x, y):
    scenic_score = 0
    for _y in range(y-1, -1, -1):
        if _y == -1:
            break
        if tree > forrest[_y][x]:
            scenic_score += 1
        else:
            scenic_score += 1
            break
    return scenic_score


def scenic_score_right(forrest, tree, x, y, size):
    scenic_score = 0
    for _x in range(x+1, size, 1):
        if _x == size:
            break
        if tree > forrest[y][_x]:
            scenic_score += 1
        else:
            scenic_score += 1
            break
    return scenic_score


def scenic_score_left(forrest, tree, x, y):
    scenic_score = 0
    for _x in range(x-1, -1, -1):
        if _x == -1:
            break
        if tree > forrest[y][_x]:
            scenic_score += 1
        else:
            scenic_score += 1
            break
    return scenic_score


def scenic_score_down(forrest, tree, x, y, size):
    scenic_score = 0
    for _y in range(y+1, size, 1):
        if _y == size:
            print("is size")
            break
        if tree > forrest[_y][x]:
            scenic_score += 1
        else:
            scenic_score += 1
            break
    return scenic_score


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    forrest = []

    for line in file_data:
        tree_line = []
        for x in line:
            tree_line.append(int(x))
        forrest.append(tree_line)

    size = len(forrest[0])
    best_scenic_score = 0
    for y, tree_line in enumerate(forrest):
        for x, tree in enumerate(tree_line):
            scenic_score = 1
            scenic_score *= scenic_score_up(forrest, tree, x, y)
            scenic_score *= scenic_score_right(forrest, tree, x, y, size)
            scenic_score *= scenic_score_left(forrest, tree, x, y)
            scenic_score *= scenic_score_down(forrest, tree, x, y, size)

            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score

    return best_scenic_score


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
