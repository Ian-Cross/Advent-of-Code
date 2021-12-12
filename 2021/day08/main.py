from reused import arguments, read_file

PATH = "2021/day08/test.txt"

digit_counts = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5]
special_digits = [2, 3, 4, 7]


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    count = 0
    for data in file_data:
        (_, display) = data.split('|')

        digits = [digit for digit in display.strip().split(' ')]
        for digit in digits:
            if len(digit) in special_digits:
                count += 1

    return count


def trim_identified(array):
    return list(filter(lambda _: _ is not None, array))


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    total = 0
    # Iterate through the segment file
    for data in file_data:
        (encoded, display) = data.split('|')
        encoded = encoded.strip().split(" ")

        decoded = {}
        mappings = {}

        # Identify the unique digits
        for digit in encoded:
            side = [_ for _ in digit]

            if (len(side) in special_digits):
                decoded[str(digit_counts.index(len(side)))] = side
                digit = None
        encoded = trim_identified(encoded)

        # Identify position a from the part of digit 7 not in digit 1
        mappings['a'] = list(
            filter(lambda _: _ not in decoded['1'], decoded['7']))

        # Identify digit 5, using the parts of digit 4 not included digit 1
        parts_of_four = list(
            filter(lambda _: _ not in decoded['1'], decoded['4']))
        for i in range(len(encoded)):
            side = [c for c in encoded[i]]
            if len(side) == 5 and set(parts_of_four).issubset(side):
                decoded['5'] = side
                encoded[i] = None
                break
        encoded = trim_identified(encoded)

        # Identify position f from the part of digit 1 in digit 5
        mappings['f'] = list(filter(lambda _: _ in decoded['1'], decoded['5']))
        # Identify position c from the part of digit 1 that isn't f
        mappings['c'] = list(
            filter(lambda _: _ not in mappings['f'], decoded['1']))

        # Identify position e from the parts of digit 8 not in digit 5 and not already identified
        potential_e = list(
            filter(lambda _: _ not in decoded['5'], decoded['8']))
        mappings['e'] = list(
            filter(lambda _: _ not in mappings['c'], potential_e))

        # Identify position e from the parts of digit 8 not in digit 5 and not already identified
        potential_g = list(
            filter(lambda _: _ not in decoded['4'], decoded['8']))
        mappings['g'] = list(
            filter(lambda _: _ not in [mappings['e'][0], mappings['a'][0]], potential_g))

        # Identify digit 0, and position b using the already identified mappings
        for digit in encoded:
            side = [_ for _ in digit]
            if len(side) == 6:
                potential_0 = list(
                    filter(lambda _: _ not in [mappings[map][0] for map in mappings], side))
                if len(potential_0) == 1:
                    mappings['b'] = potential_0
                    decoded['0'] = side
                    digit = None
                    break
        encoded = trim_identified(encoded)

        # Identify position d from the parts of digit 8 not in digit 0
        mappings['d'] = list(
            filter(lambda _: _ not in decoded['0'], decoded['8']))

        # Catch the leftovers digits with the completed mapping
        proper_digit_mappings = {
            '2': ['a', 'c', 'd', 'e', 'g'],
            '3': ['a', 'c', 'd', 'f', 'g'],
            '6': ['a', 'b', 'd', 'e', 'f', 'g'],
            '9': ['a', 'b', 'c', 'd', 'f', 'g']
        }
        for digit_map in proper_digit_mappings:
            digit = [mappings[_][0] for _ in proper_digit_mappings[digit_map]]
            digit.sort()

            for i, num in enumerate(encoded):
                if num == None:
                    continue

                side = [_ for _ in num]
                side.sort()
                if (side == digit):
                    decoded[digit_map] = side
                    encoded[i] = None

        # Decode the displayed digits
        number = ''
        for digits in display.split(" "):
            num = [_ for _ in digits.strip()]
            num.sort()
            if len(num) == 0:
                continue
            for digit in decoded:
                decoded[digit].sort()
                if decoded[digit] == num:
                    number += digit
        total += int(number)
    return total


if __name__ == "__main__":
    print(arguments(part1, part2))
    print("\n")
