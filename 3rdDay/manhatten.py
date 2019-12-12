import re
from operator import itemgetter

input_file = open("input.txt","r")

X = 0
Y = 1
directions = {"U":[0,1],"L":[-1,0],"D":[0,-1],"R":[1,0]}

wires = []
polar_wires = []
numSteps = 0

for wire in input_file:
    wires.append(wire.strip().split(","))

def to_polar(polar_wire, command):
    global numSteps
    dir = re.findall("[a-zA-Z]",command)[0]
    length = re.findall("[0-9]+",command)[0]
    for i in range(int(length)):
        curr_loc = polar_wire[-1]
        numSteps += 1
        polar_wire.append([curr_loc[X] + directions[dir][X],curr_loc[Y] + directions[dir][Y], numSteps])

for wire in wires:
    polar_wire = [[0,0,0]]
    numSteps = 0
    for direction in wire:
        to_polar(polar_wire,direction)
    polar_wires.append(polar_wire)

for wire in polar_wires:
    wire.sort(key=itemgetter(Y))
    wire.sort(key=itemgetter(X))

wire_1_curr_pos = 0
wire_2_curr_pos = 0
wire_1_length = len(polar_wires[0])
wire_2_length = len(polar_wires[1])
wire_1 = polar_wires[0]
wire_2 = polar_wires[1]
matching_points = []
while True:
    if wire_1_curr_pos == wire_1_length or wire_2_curr_pos == wire_2_length:
        break
    if wire_1[wire_1_curr_pos][X] == wire_2[wire_2_curr_pos][X] and wire_1[wire_1_curr_pos][Y] == wire_2[wire_2_curr_pos][Y]:
        wire_1[wire_1_curr_pos].append(wire_2[wire_2_curr_pos][2])
        matching_points.append(wire_1[wire_1_curr_pos])
        wire_1_curr_pos+=1
        wire_2_curr_pos+=1
    elif wire_1[wire_1_curr_pos][X] == wire_2[wire_2_curr_pos][X] and wire_1[wire_1_curr_pos][Y] < wire_2[wire_2_curr_pos][Y]:
        wire_1_curr_pos+=1
    elif wire_1[wire_1_curr_pos][X] == wire_2[wire_2_curr_pos][X] and wire_1[wire_1_curr_pos][Y] > wire_2[wire_2_curr_pos][Y]:
        wire_2_curr_pos+=1
    elif wire_1[wire_1_curr_pos][X] < wire_2[wire_2_curr_pos][X]:
        wire_1_curr_pos+=1
    elif wire_1[wire_1_curr_pos][X] > wire_2[wire_2_curr_pos][X]:
        wire_2_curr_pos+=1

print(matching_points)

smallest_manhatten = 0
smallest_steps = 0
for point in matching_points:
    curr_manhatten = abs(point[X]) + abs(point[Y])
    curr_steps = point[2] + point[3]
    if curr_steps < smallest_steps or smallest_steps == 0:
        smallest_steps = curr_steps
    if curr_manhatten < smallest_manhatten or smallest_manhatten == 0:
        smallest_manhatten = curr_manhatten

print(smallest_manhatten)
print(smallest_steps)
