from reused import arguments, read_file
import operator
import math

PATH = "2022/day11/test.txt"
NUM_ROUNDS = 10000
NUM_TRAILS = 100
monkeys = []


class Item:
    def __init__(self, worry_level):
        self.worry_level = worry_level

    def __str__(self) -> str:
        return str(self.worry_level)

    def __repr__(self) -> str:
        return f"<Item w={self.worry_level} />"


class Monkey:
    num_inspected = 0

    def __init__(self, id, items, op, test):
        self.id = id
        self.items = items
        self.op = op
        self.test = test

    def inspect_items(self, calm):
        LHS, RHS = None, None
        while len(self.items) != 0:
            item = self.items.pop(0)
            self.num_inspected += 1
            if self.op['LHS'][0].isdigit():
                LHS = int(self.op['LHS'])
            else:
                LHS = item.worry_level

            if self.op['RHS'][0].isdigit():
                RHS = int(self.op['RHS'])
            else:
                RHS = item.worry_level

            if calm:
                item.worry_level = math.floor(self.op['op'](LHS, RHS)/3)
            else:
                item.worry_level = math.floor(self.op['op'](LHS, RHS))
            self.test_item(item)

    def test_item(self, item):
        global monkeys
        monkeys[self.test[item.worry_level %
                          self.test['val'] == 0]].items.append(item)


def display_monkeys():
    for monkey in monkeys:
        print(
            f"Monkey: {monkey.id}: {' '.join([str(item) for item in monkey.items])}")


def compare_monkeys(initial_state):
    for i in range(len(monkeys)):
        a = [item.worry_level for item in monkeys[i].items]
        b = [item.worry_level for item in initial_state[i].items]
        if a != b:
            return False
    return True


def define_monkey(monkey_details):
    id = int(monkey_details[0].split(" ")[1][0])
    items = []
    for item in monkey_details[1].strip().split(" "):
        if item[0].isdigit():
            items.append(Item(int(item[:2])))

    op_details = monkey_details[2].strip().split(" ")[3:]
    op = {
        'LHS': op_details[0],
        'op': operator.add if op_details[1] == "+" else operator.mul,
        'RHS': op_details[2]
    }

    test = {
        'val': int(monkey_details[3].strip().split(" ")[-1]),
        True: int(monkey_details[4].strip().split(" ")[-1]),
        False: int(monkey_details[5].strip().split(" ")[-1]),
    }

    return Monkey(id, items, op, test)


def part1(path):
    global monkeys, NUM_ROUNDS
    NUM_ROUNDS = 20
    file_data = read_file(path or PATH, return_type=str, as_one=True)

    monkey_text = file_data.split("\n\n")
    monkeys = []
    for monkey in monkey_text:
        monkey_details = monkey.split("\n")
        monkeys.append(define_monkey(monkey_details))

    for round in range(NUM_ROUNDS):
        for monkey in monkeys:
            monkey.inspect_items(calm=True)
        display_monkeys()

    most_active_monkeys = [0, 0]
    for monkey in monkeys:
        if monkey.num_inspected > most_active_monkeys[0]:
            most_active_monkeys.insert(0, monkey.num_inspected)
            most_active_monkeys.pop()
        elif monkey.num_inspected > most_active_monkeys[0]:
            most_active_monkeys.insert(1, monkey.num_inspected)
            most_active_monkeys.pop()
    return most_active_monkeys[0]*most_active_monkeys[1]


def part2(path):
    global monkeys, NUM_ROUNDS

    file_data = read_file(path or PATH, return_type=str, as_one=True)

    monkey_text = file_data.split("\n\n")
    monkeys = []
    initial_monkey_state = []

    for monkey in monkey_text:
        monkeys.append(define_monkey(monkey.split("\n")))
        initial_monkey_state.append(define_monkey(monkey.split("\n")))

    for round in range(NUM_ROUNDS):
        for monkey in monkeys:
            monkey.inspect_items(calm=False)
        print(round)

    most_active_monkeys = [0, 0]
    for monkey in monkeys:
        if monkey.num_inspected > most_active_monkeys[0]:
            most_active_monkeys.insert(0, monkey.num_inspected)
            most_active_monkeys.pop()
        elif monkey.num_inspected > most_active_monkeys[0]:
            most_active_monkeys.insert(1, monkey.num_inspected)
            most_active_monkeys.pop()
    return most_active_monkeys[0]*most_active_monkeys[1]


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
