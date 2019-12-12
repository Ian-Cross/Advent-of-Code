from reused import arguments, readFile
import re
from operator import itemgetter

PATH = "3rdDay/input.txt"

X = 0
Y = 1
directions = {"U":[0,1],"L":[-1,0],"D":[0,-1],"R":[1,0]}
numSteps = 0

"""
Desc: Convert a directional direction command into the correct number of polar coordinates (i.e. U2 = [(0,1),(0,2)])
Param: polar_wire: list, Containing all of the polar coordinates from the origin
       command: string, containing the direction and magnitude of the wire
"""
def to_polar(polar_wire, command):
    global numSteps
    # Split apart the direction and the magnitude
    dir = re.findall("[a-zA-Z]",command)[0]
    length = int(re.findall("[0-9]+",command)[0])
    # Apply the direction the required amount of times
    for i in range(length):
        curr_loc = polar_wire[-1]
        numSteps += 1
        polar_wire.append([curr_loc[X] + directions[dir][X],curr_loc[Y] + directions[dir][Y], numSteps])


"""
Desc: Look through the two wires and identify matching points between them
Param: polar_wires, a list of polar coordinates
"""
def getMatchingPoints(polar_wires):
    wire_1_curr_pos = 0
    wire_2_curr_pos = 0
    wire_1_length = len(polar_wires[0])
    wire_2_length = len(polar_wires[1])
    wire_1 = polar_wires[0]
    wire_2 = polar_wires[1]
    matching_points = []
    while True:
        # Exit once reaching the end of either wire
        if wire_1_curr_pos == wire_1_length or wire_2_curr_pos == wire_2_length:
            break
        # Append the matching point to a list, with the steps from both wires
        if wire_1[wire_1_curr_pos][X] == wire_2[wire_2_curr_pos][X] and wire_1[wire_1_curr_pos][Y] == wire_2[wire_2_curr_pos][Y]:
            wire_1[wire_1_curr_pos].append(wire_2[wire_2_curr_pos][2])
            matching_points.append(wire_1[wire_1_curr_pos])
            wire_1_curr_pos+=1
            wire_2_curr_pos+=1
        # Increment the position tracker on the wire that has smaller coordinates
        elif wire_1[wire_1_curr_pos][X] == wire_2[wire_2_curr_pos][X] and wire_1[wire_1_curr_pos][Y] < wire_2[wire_2_curr_pos][Y]:
            wire_1_curr_pos+=1
        elif wire_1[wire_1_curr_pos][X] == wire_2[wire_2_curr_pos][X] and wire_1[wire_1_curr_pos][Y] > wire_2[wire_2_curr_pos][Y]:
            wire_2_curr_pos+=1
        elif wire_1[wire_1_curr_pos][X] < wire_2[wire_2_curr_pos][X]:
            wire_1_curr_pos+=1
        elif wire_1[wire_1_curr_pos][X] > wire_2[wire_2_curr_pos][X]:
            wire_2_curr_pos+=1
    return matching_points


"""
Desc: Intake descriptions of two wires and identify the closest intersection by manhatten distance
Param: path: a filepath to the input data
"""
def part_1(path):
    wires = readFile(path or PATH,return_type=str,strip=True,split=",")
    polar_wires = []

    for wire in wires:
        polar_wire = [[0,0,0]]
        for direction in wire:
            to_polar(polar_wire,direction)
        polar_wires.append(polar_wire)

    # sort the wires by Y then X values to derive an always incrementing pattern
    for wire in polar_wires:
        wire.sort(key=itemgetter(Y))
        wire.sort(key=itemgetter(X))

    matching_points = getMatchingPoints(polar_wires)

    # Iterate through the matching points to calculate the smallest distance
    smallest_manhatten = 0
    for point in matching_points:
        curr_manhatten = abs(point[X]) + abs(point[Y])
        if curr_manhatten < smallest_manhatten or smallest_manhatten == 0:
            smallest_manhatten = curr_manhatten

    print("The Manhattan distance from the central port to the closest intersection is %d" % smallest_manhatten)


"""
Desc: Intake descriptions of two wires and identify the closest intersection by number of "steps" for each wire to get there
Param: path: a filepath to the input data
"""
def part_2(path):
    global numSteps

    wires = readFile(path or PATH,return_type=str,strip=True,split=",")
    polar_wires = []

    for wire in wires:
        polar_wire = [[0,0,0]]
        numSteps = 0
        for direction in wire:
            to_polar(polar_wire,direction)
        polar_wires.append(polar_wire)

    # sort the wires by Y then X values to derive an always incrementing pattern
    for wire in polar_wires:
        wire.sort(key=itemgetter(Y))
        wire.sort(key=itemgetter(X))

    matching_points = getMatchingPoints(polar_wires)

    # Iterate through the matching points to calculate the smallest number of steps
    smallest_steps = 0
    for point in matching_points:
        curr_steps = point[2] + point[3]
        if curr_steps < smallest_steps or smallest_steps == 0:
            smallest_steps = curr_steps

    print("The fewest combined steps the wires must take to reach an intersection is %d" % smallest_steps)
    pass

if __name__ == '__main__':
    arguments(part_1,part_2)
