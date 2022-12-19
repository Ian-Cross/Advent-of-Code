from reused import arguments, read_file
import re

PATH = "2022/day04/test.txt"


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    count = 0
    for line in file_data:
        ranges = re.split(',|-', line)
        if set(x for x in range(int(ranges[0]), int(ranges[1])+1)).issubset(set(x for x in range(int(ranges[2]), int(ranges[3])+1))):
            count += 1
        elif set(x for x in range(int(ranges[2]), int(ranges[3])+1)).issubset(set(x for x in range(int(ranges[0]), int(ranges[1])+1))):
            count += 1
    return count


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    count = 0
    for line in file_data:
        ranges = re.split(',|-', line)
        if set(x for x in range(int(ranges[0]), int(ranges[1])+1)) & set(x for x in range(int(ranges[2]), int(ranges[3])+1)):
            count += 1
    return count


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
