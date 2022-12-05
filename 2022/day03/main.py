from reused import arguments, read_file

PATH = "2022/day03/test.txt"


def get_priority(c):
    val = ord(c)-96
    if val < 0:
        val = ord(c)-38
    return val


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    total = 0
    for rucksack in file_data:
        half = int(len(rucksack)/2)
        match = set(rucksack[:half]) & set(rucksack[half:])
        total += get_priority(match.pop())
    return total


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    total = 0
    for x in range(0, len(file_data), 3):
        badge = set(file_data[x]) & set(file_data[x+1]) & set(file_data[x+2])
        total += get_priority(badge.pop())
    return total


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
