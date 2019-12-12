from pathlib import Path
from math import floor

input_file = Path("input.txt")

# weights = [(floor(int(line.strip())/3)-2) if line.strip().isnumeric() else 0 for line in input_file.open()]
module_weights = []
curr_weight = []

def fuel_cost(weight):
    curr_cost = floor(weight/3)-2
    if (curr_cost >= 0):
        curr_weight.append(curr_cost)
        fuel_cost(curr_cost)


for line in input_file.open():
    line = line.strip()
    if line.isnumeric():
        fuel_cost(int(line))
        module_weights.append(sum(curr_weight))
        curr_weight = []

print(sum(module_weights))
