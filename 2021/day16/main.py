from typing import BinaryIO
from reused import arguments, read_file

PATH = "2021/day16/input.txt"


def done(packet):
    for bit in packet:
        if bit == '1':
            return False
    return True


def proccess_packet(packet):
    print(packet)
    versions = [packet[:3]]
    type_id = packet[3:6]

    if type_id == '100':
        read_head = 6
        literal = ""
        while True:
            piece = packet[read_head:read_head+5]
            literal += piece[1:]
            read_head += 5
            if (piece[0] == '0'):
                break
        print(literal, int(literal, 2))
    else:
        length_type_id = packet[6]
        read_head = 7
        if (length_type_id == '0'):
            bit_length = packet[read_head:read_head+15]
            read_head += 15
            print(bit_length, int(bit_length, 2))
        elif (length_type_id == '1'):
            num_packets = packet[read_head:read_head+11]
            read_head += 11
            print(num_packets, int(num_packets, 2))

    if done(packet[read_head:]) or read_head == len(packet)-1:
        return versions
    versions += proccess_packet(packet[read_head:])
    return versions


def part1(path):
    hex = read_file(path or PATH, return_type=str, strip=True)
    binary = bin(int(hex[0], 16))[2:]

    versions = proccess_packet(binary)
    return sum([int(version, 2) for version in versions])


binary = ""


def get_length_type_id():
    length_type_id = pop(1)
    value = ""
    if (length_type_id == '0'):
        value = pop(15)
    elif (length_type_id == '1'):
        value = pop(11)
    return length_type_id, int(value, 2)


def process_by_length(length):
    decoded = []
    used = 0
    while used < length:
        resp = decode_packet()
        decoded.append(resp)
        used += resp[1]
    return decoded


def process_by_count(count):
    decoded = []
    for _ in range(count):
        resp = decode_packet()
        decoded.append(resp)
    return decoded


def pop(amount):
    global binary
    bit = binary[:amount]
    binary = binary[amount:]
    return bit


def done():
    for bit in binary:
        if bit == '1':
            return False
    return True


def decode_packet():
    if (done()):
        return (0, 0)
    version = pop(3)
    type_id = pop(3)
    count = 6
    
    # Literal Value of Type 4
    if type_id == '100':
        literal = ""
        while True:
            piece = pop(5)
            count += 5
            literal += piece[1:]
            if (piece[0] == '0'):
                break
        return int(literal, 2), count
    else:
        length_type_id, length_value = get_length_type_id()
        if length_type_id == '0':
            response = process_by_length(length_value)
            count += 16
        elif length_type_id == '1':
            response = process_by_count(length_value)
            count += 12

        # Sum values type 0
        if type_id == "000":
            sum = 0
            for val in response:
                sum += val[0]
                count += val[1]
            return sum, count

        # Product values type 1
        elif type_id == "001":
            product = 1
            for val in response:
                product *= val[0]
                count += val[1]
            return product, count

        # Min values type 2
        elif type_id == "010":
            min = 9999999999999
            for val in response:
                count += val[1]
                if val[0] < min:
                    min = val[0]
            return min, count

        # Max values type 3
        elif type_id == "011":
            max = 0
            for val in response:
                count += val[1]
                if val[0] > max:
                    max = val[0]
            return max, count

        # Greater Than values type 5
        elif type_id == "101":
            count += response[0][1] + response[1][1]
            return int(response[0][0] > response[1][0]), count

        # Less Than values type 6
        elif type_id == "110":
            count += response[0][1] + response[1][1]
            return int(response[0][0] < response[1][0]), count

        # Equal to values type 7
        elif type_id == "111":
            count += response[0][1] + response[1][1]
            return int(response[0][0] == response[1][0]), count


def part2(path):
    global binary
    hex = read_file(path or PATH, return_type=str, strip=True)

    binary = bin(int(hex[0], 16))[2:].zfill(4)
    packets = decode_packet()
    return packets[0]


if __name__ == "__main__":
    print(arguments(part1, part2))
    print("\n")
