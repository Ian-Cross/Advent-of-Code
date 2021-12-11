from reused import arguments, read_file

PATH = "2021/day10/test.txt"
OPENERS = ['(', '[', '{', '<']
CLOSERS = [')', ']', '}', '>']


def is_corrupt(line):
    pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
    char_stack = []
    for c in line:
        if c in OPENERS:
            char_stack.append(c)
        elif c in CLOSERS:
            if pairs[c] != char_stack[-1]:
                return c
            char_stack = char_stack[:-1]
    return None


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    points = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0}
    return sum([points[is_corrupt(line)] for line in file_data])


def correct_line(line):
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    char_stack = []
    for c in line:
        if c in OPENERS:
            char_stack.append(c)
        elif c in CLOSERS:
            char_stack = char_stack[:-1]

    return [pairs[c] for c in reversed(char_stack)]


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    points = {')': 1, ']': 2, '}': 3, '>': 4}

    inc_lines = [line for line in file_data if is_corrupt(line) is None]

    sums = []
    for line in inc_lines:
        correction = correct_line(line)
        sum = 0
        for c in correction:
            sum *= 5
            sum += points[c]
        sums.append(sum)
    sums.sort()
    return sums[int(len(sums)/2)]


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
