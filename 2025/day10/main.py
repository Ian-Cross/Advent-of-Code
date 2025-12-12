from reused import arguments, read_file
from collections import deque
import pulp

PATH = "2025/day10/test.txt"


def min_pesses_toggle(lights, buttons):
    N = len(lights)
    goal = int("".join(["1" if i == "#" else "0" for i in lights]), 2)
    start = 0
    buttons_masks = []
    for button in buttons:
        mask = 0
        for b in button:
            mask |= 1 << (N - 1 - int(b))
        buttons_masks.append(mask)

    visited = set()
    queue = deque([(start, 0)])
    while queue:
        state, presses = queue.popleft()
        if state == goal:
            return presses
        for button in buttons_masks:
            new_state = state ^ button
            if new_state in visited:
                continue
            visited.add(new_state)
            queue.append((new_state, presses + 1))

def min_presses_sum(buttons, goal):
    N = len(goal)
    M = len(buttons)

    # set up the linear programming problem
    prob = pulp.LpProblem("Joltage", pulp.LpMinimize) # sets the goal to minimize
    # creates a variable to represent the number of times each button is pressed
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(M)]
    # final objective is to minimize the sum of all button presses
    prob += pulp.lpSum(x)

    # build out the system of equations, one for each light
    # Take the part of each buttont that affects that light and ensure it matches the goal
    for j in range(N):
        prob += pulp.lpSum(x[i] if j in buttons[i] else 0 for i in range(M)) == goal[j]
    
    # solve the problem
    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[prob.status] == "Optimal":
        return int(pulp.value(prob.objective))
    else:
        return -1  # No solution


def part1(path):
    file_data = read_file(path or PATH, return_type=str, strip=True, split=" ")

    total = 0
    for line in file_data:
        lights = line[0][1:-1]
        buttons = [button[1:-1].split(",") for button in line[1:-1]]
        total += min_pesses_toggle(lights, buttons)

    return total


def part2(path):
    file_data = read_file(path or PATH, return_type=str, strip=True, split=" ")

    total = 0
    for line in file_data:
        buttons = [[int(b) for b in button[1:-1].split(",")] for button in line[1:-1]]
        joltages = [int(j) for j in line[-1][1:-1].split(",")]
        total += min_presses_sum(buttons, joltages)

    return total


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
