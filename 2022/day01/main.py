from reused import arguments, read_file

PATH = "2022/day01/test.txt"


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    print(file_data)

    elf_totals = []
    buffer = 0
    for row in file_data:
        if (row == ''):
            elf_totals.append(buffer)
            buffer = 0
        else:
            buffer += int(row)
    elf_totals.append(buffer)
    elf_totals.sort()
    print(elf_totals[-1])


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    print(file_data)

    elf_totals = []
    buffer = 0
    for row in file_data:
        if (row == ''):
            elf_totals.append(buffer)
            buffer = 0
        else:
            buffer += int(row)
    elf_totals.append(buffer)
    elf_totals.sort()
    print(sum(elf_totals[-3:]))


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
