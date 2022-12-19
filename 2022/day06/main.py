from reused import arguments, read_file

PATH = "2022/day06/test.txt"


def all_diff(buff, size):
    if len(set(buff)) == size:
        return True
    return False


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    buffer = []
    size = 4
    for i, c in enumerate(file_data[0]):
        buffer.append(c)
        if len(buffer) > size:
            buffer.pop(0)
            if (all_diff(buffer, size)):
                return i+1


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    buffer = []
    size = 14
    for i, c in enumerate(file_data[0]):
        buffer.append(c)
        if len(buffer) > size:
            buffer.pop(0)
            if (all_diff(buffer, size)):
                return i+1


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
