from reused import arguments, read_file
import re

PATH = "2021/day17/input.txt"


def overshot(x_pos, y_pos, target):
    left, top, right, bottom = target
    if x_pos > right:
        return True
    if y_pos < bottom:
        return True
    return False


def in_target(x_pos, y_pos, target):
    left, top, right, bottom = target
    if x_pos > right or x_pos < left:
        return False
    if y_pos > top or y_pos < bottom:
        return False
    return True


def shoot(y_v, x_v, target):
    x_pos, y_pos = 0, 0
    max_y_pos = 0
    while not overshot(x_pos, y_pos, target):
        y_pos += y_v
        y_v -= 1
        max_y_pos = max(max_y_pos, y_pos)

        x_pos += x_v
        if x_v > 0:
            x_v -= 1

        if (in_target(x_pos, y_pos, target)):
            return True, max_y_pos
    return False, 0


def get_target(file_data):
    left, right, top, bottom = 0, 0, 0, 0
    try:
        search = re.findall("([x|y]=(-?[0-9]*)..(-?[0-9]*))", file_data[0])
        if len(search) != 2:
            return
        left, right = int(search[0][1]), int(search[0][2])
        bottom, top = int(search[1][1]), int(search[1][2])
    except:
        return
    return left, top, right, bottom


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    target = get_target(file_data)

    max_y_pos = 0
    for y_v in range(-200, 200):
        for x_v in range(0, 200):
            hit, local_max_y_pos = shoot(y_v, x_v, target)
            if hit:
                max_y_pos = max(local_max_y_pos, max_y_pos)

    return max_y_pos


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    target = get_target(file_data)

    count = 0
    for y_v in range(-200, 200):
        for x_v in range(0, 200):
            hit, _ = shoot(y_v, x_v, target)
            if hit:
                count += 1
    return count


if __name__ == "__main__":
    print(arguments(part1, part2))
    print("\n")
