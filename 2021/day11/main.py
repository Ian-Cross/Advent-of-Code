from reused import arguments, read_file

PATH = "2021/day11/test.txt"
ADJ = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def charge(octopi):
    for y, row in enumerate(octopi):
        for x, col in enumerate(row):
            if col+1 == 10:
                octopi[y][x] = 0
            else:
                octopi[y][x] += 1
    return octopi


def display(octopi):
    for row, _ in enumerate(octopi):
        for col, _ in enumerate(octopi[row]):
            print(str(octopi[row][col]), end=" ")
        print()
    print()


def in_bounds(row, col, octopi):
    if row < 0 or row >= len(octopi):
        return False
    if col < 0 or col >= len(octopi[row]):
        return False
    return True


def flash_neighbours(y, x, octopi):
    for (row, col) in ADJ:
        if (not in_bounds(y + row, x + col, octopi)):
            continue

        val = octopi[y + row][x + col]
        if (val + 1 == 10):
            octopi[y + row][x + col] = 10
            octopi = flash_neighbours(y + row, x + col, octopi)
        elif (val == 0 or val == 10):
            pass
        else:
            octopi[y + row][x + col] += 1
    return octopi


def flash(octopi):
    for row, _ in enumerate(octopi):
        for col, _ in enumerate(octopi[row]):
            if (octopi[row][col] == 0):
                octopi = flash_neighbours(row, col, octopi)
    return octopi


def count(octopi):
    flashes = 0
    for row, _ in enumerate(octopi):
        for col, _ in enumerate(octopi[row]):
            if octopi[row][col] == 10 or octopi[row][col] == 0:
                octopi[row][col] = 0
                flashes += 1
    return (octopi, flashes)


def build_matrix(file_data):
    octopi = []
    for line in file_data:
        row = []
        for oct in line:
            row.append(int(oct))
        octopi.append(row)
    return octopi


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    octopi = build_matrix(file_data)

    steps = 100
    total_flashes = 0
    for _ in range(steps):
        octopi = charge(octopi)
        octopi = flash(octopi)
        (octopi, flashes) = count(octopi)
        total_flashes += flashes
    return total_flashes


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    octopi = build_matrix(file_data)

    step = 0
    while True:
        octopi = charge(octopi)
        octopi = flash(octopi)
        (octopi, flashes) = count(octopi)
        step += 1
        if (flashes == len(octopi)*len(octopi)):
            break
    return step


if __name__ == "__main__":
    print(arguments(part1, part2))
    print("\n")
