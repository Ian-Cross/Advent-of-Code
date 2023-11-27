from reused import arguments, read_file
import re

PATH = "2022/day15/test.txt"


def is_numeric(w):
    try:
        float(w)
    except ValueError:
        return False
    return True


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    sensor_data = set()
    beacons = set()

    line_key = 2000000
    # line_key = 10

    for line in file_data:
        details = [int(x)
                   for x in re.split(r" |,|=|:", line) if is_numeric(x)]

        sensor = tuple(details[0:2])
        beacon = tuple(details[2:])
        beacons.add(beacon)

        distance_to_beacon = abs(
            sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        distance_to_line_key = line_key - sensor[1]

        i = 0
        while abs(distance_to_line_key) + i <= distance_to_beacon:
            new_pos_pos = tuple(
                map(sum, zip(sensor, (i, distance_to_line_key))))
            new_pos_neg = tuple(
                map(sum, zip(sensor, (-i, distance_to_line_key))))

            if new_pos_pos not in beacons:
                sensor_data.add(new_pos_pos)
            if new_pos_neg not in beacons:
                sensor_data.add(new_pos_neg)

            i += 1
    print(len(sensor_data))


def print_sensor_data(sensor_data, sensors, beacons):
    for x in range(0, 20):
        for y in range(0, 20):

            if ((x, y) in sensors):
                print('S', end='')
            elif ((x, y) in beacons):
                print('B', end='')
            elif ((x, y) in sensor_data):
                print('#', end='')
            else:
                print('.', end='')
        print()


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)

    sensor_data = set()
    beacons = set()
    sensors = set()

    line_key = 4000000

    for line in file_data:
        details = [int(x)
                   for x in re.split(r" |,|=|:", line) if is_numeric(x)]

        sensor = tuple(details[0:2])
        sensors.add(sensor)
        beacon = tuple(details[2:])
        beacons.add(beacon)

        distance_to_beacon = abs(
            sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        for j in range(-distance_to_beacon, distance_to_beacon):
            if j < 0 or j > line_key:
                continue

            i = 0
            while abs(j) + i <= distance_to_beacon:
                if abs(j) + i >:
                new_pos_pos = tuple(
                    map(sum, zip(sensor, (i, j))))
                new_pos_neg = tuple(
                    map(sum, zip(sensor, (-i, j))))

                if new_pos_pos not in beacons:
                    sensor_data.add(new_pos_pos)
                if new_pos_neg not in beacons:
                    sensor_data.add(new_pos_neg)

                # print_sensor_data(sensor_data, sensors, beacons)
                # input()

                i += 1
    for x in range(0, line_key):
        for y in range(0, line_key):
            if (x, y) in sensor_data or (x, y) in beacons:
                continue
            else:
                print((x, y))
    # print_sensor_data(sensor_data, sensors, beacons)


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
