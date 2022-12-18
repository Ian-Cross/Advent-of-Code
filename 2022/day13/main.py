from reused import arguments, read_file

PATH = "2022/day13/test.txt"


LIST_START = '['
LIST_END = ']'
LIST_ITEM = ','

data = ""


class Packet:
    def __init__(self, is_list=False, is_int=False, val=-1, depth=0, build=False, children=[]):
        global data
        self.is_list = is_list
        self.is_int = is_int
        self.children = []
        self.val = val
        self.depth = depth
        self.s = ''.join(data)
        if build:
            self.build_packet(depth)

    def __repr__(self) -> str:
        if self.is_list:
            return f"<Packet list chilren={len(self.children)} str='{self.s}'/>"
        elif self.is_int:
            return f"<Packet int val={self.val} />"
        else:
            return f"<Packet />"

    def __lt__(self, other):
        return compare_pair(self, other) == 1

    def build_packet(self, depth):
        val_buf = ''
        while len(data) != 0:
            i = data.pop(0)
            # for _ in range(depth):
            #     print(f"\t", end='')
            # print(f"{i}", end=': ')
            if i == LIST_START:
                # print("list start")
                if self.is_list:
                    data.insert(0, i)
                    self.children.append(Packet(build=True, depth=depth+1))
                else:
                    self.is_list = True
            elif i.isdigit():
                # print(f"digit:{val_buf}")
                val_buf += i
            elif i == LIST_ITEM:
                if val_buf != '':
                    # print(f":{self.is_list}:", end='')
                    # print(f"end of child: {val_buf}")
                    child = Packet(is_int=True, val=int(
                        val_buf), depth=depth+1)
                    val_buf = ''
                    self.children.append(child)
            elif i == LIST_END:
                if val_buf != '':
                    # print(f":{self.is_list}:", end='')
                    # print(f"end of child: {val_buf}")
                    child = Packet(is_int=True, val=int(
                        val_buf), depth=depth+1)
                    val_buf = ''
                    self.children.append(child)
                return


def compare_pair(LHS, RHS):
    # for _ in range(LHS.depth):
    # print(f"\t", end='')
    # print(f"Comparing, {LHS},{RHS}", end=':')
    if LHS.is_int and RHS.is_int:
        # print(f"\t comparing ints", end=',')
        if LHS.val < RHS.val:
            # print(" right")
            return 1
        elif LHS.val > RHS.val:
            # print(" wrong")
            return -1
        else:
            # print(f" unsure")
            return 0

    if LHS.is_int and RHS.is_list:
        # print(f" converting LHS - {LHS}", end=' ')
        temp = LHS
        LHS = Packet(is_list=True)
        LHS.children.append(temp)
        # print(f" - {LHS}", end=' ')
    elif LHS.is_list and RHS.is_int:
        # print(f" converting RHS - {RHS}", end=' ')
        temp = RHS
        RHS = Packet(is_list=True)
        RHS.children.append(temp)
        # print(f" - {RHS}", end=' ')

    if LHS.is_list and RHS.is_list:
        # print(f"\t comparing lists")
        i, j = 0, 0
        while i < len(LHS.children) and j < len(RHS.children):
            res = compare_pair(LHS.children[i], RHS.children[j])
            if (res == 1):
                # print(f"\t right,")
                return 1
            if (res == -1):
                # print(f"\t wrong,")
                return -1

            i += 1
            j += 1
        if i == len(LHS.children) and j < len(RHS.children):
            # print(f"\t right,")
            return 1
        if i < len(LHS.children) and j == len(RHS.children):
            # print(f"\t wrong,")
            return -1


def part1(path):
    global data
    file_data = read_file(path or PATH, return_type=str, strip=True)

    pairs = []
    new_pair = [None, None]
    for line in file_data:
        if line == '':
            pairs.append(new_pair)
            new_pair = [None, None]
        elif new_pair[0] == None:
            new_pair[0] = line

        elif new_pair[1] == None:
            new_pair[1] = line

    indices = []
    for idx, pair in enumerate(pairs):
        data = [c for c in pair[0]]
        left_packet = Packet(build=True, depth=0)

        data = [c for c in pair[1]]
        right_packet = Packet(build=True, depth=0)

        if compare_pair(left_packet, right_packet) == 1:
            indices.append(idx+1)
    print(sum(indices))


def part2(path):
    global data
    divider_packets = ['[[2]]', '[[6]]']
    file_data = read_file(path or PATH, return_type=str, strip=True)

    packets = []
    for line in file_data:
        if line == '':
            continue
        data = [c for c in line]
        packets.append(Packet(build=True, depth=0))

    for d in divider_packets:
        data = [c for c in d]
        packets.append(Packet(build=True, depth=0))

    packets.sort()

    indices = []
    for idx, packet in enumerate(packets):
        if packet.s in divider_packets:
            indices.append(idx+1)

    print(indices[0]*indices[1])


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
