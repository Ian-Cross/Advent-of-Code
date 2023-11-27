from reused import arguments, read_file

PATH = "2022/day12/test.txt"
START_CHAR = 'S'
END_CHAR = 'E'

starting_spots = []
height_map = []
process_queue = []
visited = set()
start = None
end = None

NEIGHBOURS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def insert_global_child(new_child):
    global process_queue
    if process_queue == []:
        process_queue.append(new_child)
        return

    # for idx, child in enumerate(process_queue):
    #     if new_child.distance_to_end < child.distance_to_end:
    #         process_queue.insert(idx, new_child)
    #         return
    process_queue.append(new_child)


class Node:
    def __init__(self, pos=(0, 0), height='a', steps=0, parent=None):
        self.pos = pos
        self.height = height
        self.steps = steps
        self.distance_to_end = 0
        self.parent = parent
        self.children = []

    def insert_child(self, new_child):
        if self.children == []:
            self.children.append(new_child)
            return

        for idx, child in enumerate(self.children):
            if new_child.distance_to_end < child.distance_to_end:
                self.children.insert(idx, new_child)
                return
        self.children.append(new_child)


def build_map(data):
    global height_map, start, end
    for y, line in enumerate(data):
        row = []
        for x, c in enumerate(line):
            if c == START_CHAR:
                c = 'a'
                start = Node((y, x), c)
            if c == END_CHAR:
                c = 'z'
                end = Node((y, x), c)
            row.append(c)
        height_map.append(row)


def print_map(visited):
    for y, row in enumerate(height_map):
        for x, col in enumerate(row):
            if (y, x) in visited:
                print("X", end='')
            else:
                print(col, end='')
        print()


def distance_from_end(node):
    return abs(end.pos[0] - node.pos[0]) + abs(end.pos[1] - node.pos[1])


def map_at(pos):
    if pos[0] < 0 or pos[0] >= len(height_map):
        return None
    if pos[1] < 0 or pos[1] >= len(height_map[0]):
        return None
    return height_map[pos[0]][pos[1]]


def walk(current):
    # print(f"curr: {current.pos},{current.height},")

    if current.pos == end.pos:
        return current

    for neighbour in NEIGHBOURS:
        new_pos = tuple(map(sum, zip(current.pos, neighbour)))
        # print(f"\t {new_pos}:", end=' ')

        if new_pos in visited:
            # print("d")
            continue

        child = Node(new_pos, map_at(new_pos), current.steps + 1, current)
        child.distance_to_end = distance_from_end(child)

        if child.height == None:
            # print("d")
            continue
        if ord(child.height) > ord(current.height) + 1:
            # print("d")
            continue

        # print("a")
        insert_global_child(child)
    return None

def find_path(debug = False):
    global process_queue, visited, start, end, height_map

    insert_global_child(start)

    end_node = None
    while len(process_queue) != 0:
        curr = process_queue.pop(0)
        if curr.pos in visited:
            continue
        visited.add(curr.pos)
        end_node = walk(curr)

        if (debug):
            print(f"c: {len(process_queue)}, v: {len(visited)}")
            print_map(visited)
        # input()
        if end_node != None:
            break

    if end_node == None:
        # print("Failed")
        return -1

    return end_node.steps


def find_start():
    global height_map, start, end, starting_spots
    for y, line in enumerate(height_map):
        for x, c in enumerate(line):
            if c == 'a' and (y,x) not in starting_spots:
                start = Node((y,x), c)
                starting_spots.append((y,x))
                return True
    return False

def part1(path):
    global process_queue, visited, start, end, height_map

    height_map = []
    process_queue = []
    visited = set()
    start = None
    end = None

    file_data = read_file(path or PATH, return_type=str, strip=True)
    build_map(file_data)

    return find_path(debug=False)


def part2(path):
    global process_queue, visited, start, end, height_map

    height_map = []
    process_queue = []
    visited = set()
    start = None
    end = None

    file_data = read_file(path or PATH, return_type=str, strip=True)
    build_map(file_data)

    min_length = 999999999

    while find_start():
        length = find_path(debug=False)
        if length > 0 and length < min_length:
            min_length = length
        process_queue = []
        visited = set()
    return min_length


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
