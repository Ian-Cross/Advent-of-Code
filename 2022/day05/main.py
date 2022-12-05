from reused import arguments, read_file
import re

PATH = "2022/day05/test.txt"


def parse_rules_and_crates(file_data):
    stacks = [[] for _ in range(0, 10)]
    rules = []
    rules_flag = False
    for line in file_data:
        line = line.replace('\n', '')

        if len(line) == 0:
            rules_flag = True
            continue
        if line[1].isdigit():
            rules_flag = True
            continue

        line = line.split(' ')

        if rules_flag:
            rules.append([int(_) for _ in line if _.isdigit()])
        else:
            col = 0
            b = 0
            while b < len(line):
                if line[b] == '':
                    col += 1
                    b += 3
                else:
                    stacks[col].insert(0, line[b][1])
                    col += 1
                b += 1
    stacks = list(filter(lambda stack: len(stack) > 0, stacks))
    return (stacks, rules)


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=False)

    (stacks, rules) = parse_rules_and_crates(file_data)

    for [qty, fr, to] in rules:
        slice = stacks[fr-1][-qty:]
        slice.reverse()
        for _ in range(0, qty):
            stacks[fr-1].pop()
        for box in slice:
            stacks[to-1].append(box)

    return ''.join([_[-1] for _ in stacks])


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=False)

    (stacks, rules) = parse_rules_and_crates(file_data)

    for [qty, fr, to] in rules:
        slice = stacks[fr-1][-qty:]
        for _ in range(0, qty):
            stacks[fr-1].pop()
        for box in slice:
            stacks[to-1].append(box)

    return ''.join([_[-1] for _ in stacks])


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
