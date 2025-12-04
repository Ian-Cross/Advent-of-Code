from reused import arguments, read_file

PATH = "2025/day03/test.txt"

def best_joltage(joltage, battery):
    batteries = str(joltage) + str(battery)
    return max(int("".join(batteries[:i] + batteries[i+1:])) for i in range(len(batteries)))

def max_joltage(bank, N):
    joltage = int(str(bank)[:N])
    for battery in str(bank)[N:]:
        joltage = best_joltage(joltage, battery)
    return joltage

def part1(path):
    file_data = read_file(path or PATH, return_type=int, strip=True)
    return sum(max_joltage(bank, 2) for bank in file_data)

def part2(path):
    file_data = read_file(path or PATH, return_type=int, strip=True)
    return sum(max_joltage(bank, 12) for bank in file_data)


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")