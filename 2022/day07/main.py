from reused import arguments, read_file

PATH = "2022/day07/test.txt"

commands = []

DISK_SPACE = 70000000
UPDATE_SPACE = 30000000


class Node:
    def __init__(self, name='', size=0):
        self.size = size
        self.sub_dirs = {}
        self.sub_files = {}
        self.name = name


def build_tree(root):
    while len(commands) > 0:
        (p1, p2, p3) = commands.pop(0)
        if p1 == '$':
            if p2 == 'cd':
                if root == None:  # Catch first case
                    root = Node(name='/')
                elif p3 == '..':
                    return root
                else:
                    sub_root = build_tree(root.sub_dirs[p3])
                    root.size += sub_root.size
            elif p2 == 'ls':
                (_p1, _p2, _p3) = commands.pop(0)
                while _p1 != '$':
                    if _p1 == 'dir':
                        root.sub_dirs[_p2] = Node(name=_p2)
                    if _p1.isnumeric():
                        root.sub_files[_p2] = Node(name=_p2, size=int(_p1))
                        root.size += int(_p1)
                    if (len(commands) == 0):
                        break
                    (_p1, _p2, _p3) = commands.pop(0)
                if (len(commands) != 0):
                    commands.insert(0, (_p1, _p2, _p3))
    return root


def sum_tree(root):
    total = 0
    for child in root.sub_dirs:
        total += sum_tree(root.sub_dirs[child])
    if root.size < 100000:
        total += root.size
    return total


def fill_commands(file_data):
    for line in file_data:
        details = line.split() + [None]*3
        commands.append(tuple(details[:3]))


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    fill_commands(file_data)

    root = build_tree(None)

    return sum_tree(root)


dir_sizes = []


def find_greater_than(root, val):
    for child in root.sub_dirs:
        find_greater_than(root.sub_dirs[child], val)
    if int(root.size) > int(val):
        dir_sizes.append(root.size)


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True)
    fill_commands(file_data)

    root = build_tree(None)

    find_greater_than(root, UPDATE_SPACE-(DISK_SPACE-root.size))

    return min(dir_sizes)


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
