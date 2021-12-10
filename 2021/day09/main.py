from reused import arguments, read_file

PATH = "2021/day09/test.txt"
ADJ = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def build_elevation_array(data):
    height_map = []
    for line in data:
        row = []
        for digit in line:
            row.append(digit)
        height_map.append(row)
    return height_map


def out_of_bounds(array, y, x):
    if y < 0 or y >= len(array):
        return True
    if x < 0 or x >= len(array[0]):
        return True
    return False


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    height_map = build_elevation_array(file_data)

    low_points = []
    for y, _ in enumerate(height_map):
        for x, _ in enumerate(height_map[y]):
            low_flag = True
            for adj in ADJ:
                if y+adj[0] < 0 or y+adj[0] >= len(height_map):
                    continue
                if x+adj[1] < 0 or x+adj[1] >= len(height_map[0]):
                    continue

                if height_map[y][x] >= height_map[y+adj[0]][x+adj[1]]:
                    low_flag = False
                    break
            if low_flag:
                low_points.append(int(height_map[y][x]) + 1)

    return sum(low_points)


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    height_map = build_elevation_array(file_data)

    low_points = []
    for y, row in enumerate(height_map):
        for x, _ in enumerate(height_map[y]):
            low_flag = True
            for adj in ADJ:
                if out_of_bounds(height_map, y+adj[0], x+adj[1]):
                    continue
                if height_map[y][x] >= height_map[y+adj[0]][x+adj[1]]:
                    low_flag = False
                    break

            if low_flag:
                low_points.append((y, x))

    def get_adj(y, x):
        neighbours = []
        for adj in ADJ:
            if out_of_bounds(height_map, y+adj[0], x+adj[1]):
                continue
            neighbours.append((y+adj[0], x+adj[1]))
        return neighbours

    checked = []

    def find_basin(y, x):
        neighbours = get_adj(y, x)
        if len(neighbours) == 0:
            return 0

        size = 0
        for neighbour in neighbours:
            if height_map[neighbour[0]][neighbour[1]] == '9':
                continue
            if (neighbour in checked):
                continue
            checked.append(neighbour)
            size += find_basin(neighbour[0], neighbour[1]) + 1
        return size

    total_size = []
    for y, x in low_points:
        checked.append((y, x))
        total_size.append(find_basin(y, x)+1)
    total_size.sort()
    return total_size[-3] * total_size[-2] * total_size[-1]


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
