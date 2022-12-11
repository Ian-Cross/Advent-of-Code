from reused import arguments, read_file
import re
import math

PATH = "2022/day10/test.txt"


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    actions = ['noop', 'addx']
    instructions = []

    for line in file_data:
        action = line.split()[0]
        value = None
        if action == actions[1]:
            instructions.append({
                'action': action,
                'val': int(line.split()[1]),
            })
        else:
            instructions.append({
                'action': action,
            })

    cycle = 1
    register = 1
    signal_strengths = []

    check_points = [20, 60, 100, 140, 180, 220]
    in_op = False
    curr_instruction = None
    while cycle <= check_points[-1]:
        if cycle in check_points:
            signal_strengths.append(register*cycle)

        if not in_op:
            if len(instructions) == 0:
                break
            curr_instruction = instructions.pop(0)
        else:
            if curr_instruction['action'] == actions[1]:
                register += curr_instruction['val']
                cycle += 1
                in_op = False
                continue

        if curr_instruction['action'] == actions[0]:
            cycle += 1
            continue
        elif curr_instruction['action'] == actions[1]:
            cycle += 1
            in_op = True
            continue

    # print(signal_strengths)
    return sum(signal_strengths)


def draw_screen(screen):
    for y in range(6):
        for x in range(0, 40):
            print(screen[y][x], end='')
        print()


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    actions = ['noop', 'addx']
    instructions = []

    for line in file_data:
        action = line.split()[0]
        if action == actions[1]:
            instructions.append({
                'action': action,
                'val': int(line.split()[1]),
            })
        else:
            instructions.append({
                'action': action,
            })

    screen = []
    for _ in range(6):
        row = []
        for _ in range(40):
            row.append(".")
        screen.append(row)

    cycle = 0
    register = 1
    in_op = False
    curr_instruction = None
    row = 0
    while cycle < 240:
        CRT_col = cycle % 40
        CRT_row = math.floor(cycle/40)
        if CRT_col in [register-1, register, register+1]:
            screen[CRT_row][CRT_col] = "#"

        if not in_op:
            if len(instructions) == 0:
                break
            curr_instruction = instructions.pop(0)
        else:
            if curr_instruction['action'] == actions[1]:
                register += curr_instruction['val']
                cycle += 1
                in_op = False
                continue

        if curr_instruction['action'] == actions[1]:
            in_op = True
        cycle += 1

    draw_screen(screen)


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
