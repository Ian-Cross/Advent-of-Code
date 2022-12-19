from reused import arguments, read_file
from enum import Enum

PATH = "2022/day02/test.txt"

p1 = {'A': 'ROCK', 'B': 'PAPER', 'C': 'SCISSORS'}

lose_against = {'ROCK': 'SCISSORS', "PAPER": "ROCK", "SCISSORS": "PAPER"}

vals = {'ROCK': 1, 'PAPER': 2, 'SCISSORS': 3}
result = {'WIN': 6, 'LOSE': 0, 'DRAW': 3}


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    p2 = {'X': 'ROCK', 'Y': 'PAPER', 'Z': 'SCISSORS'}

    total = 0
    for line in file_data:
        a, b = line.split(" ")
        you, me = p1[a], p2[b]

        total += vals[me]

        if you == me:
            total += result['DRAW']
        elif lose_against[you] == me:
            total += result['LOSE']
        else:
            total += result['WIN']
    return total


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    outcome = {'X': 'LOSE', 'Y': 'DRAW', 'Z': 'WIN'}

    total = 0
    for line in file_data:
        a, c = line.split(" ")
        you, res = p1[a], outcome[c]

        total += result[res]
        if res == 'DRAW':
            total += vals[you]
        if res == 'WIN':
            total += vals[lose_against[lose_against[you]]]
        if res == 'LOSE':
            total += vals[lose_against[you]]
        print(total)

    return total


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
