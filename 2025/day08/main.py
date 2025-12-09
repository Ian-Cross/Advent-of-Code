import re
from reused import arguments, read_file
from collections import defaultdict
from math import sqrt, prod

PATH = "2025/day08/test.txt"

def distance_3d(p1, p2):
  return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

def distances(boxes):
  junction_boxes = {}
  for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        d = distance_3d(boxes[i], boxes[j])
        junction_boxes[(tuple(boxes[i]), tuple(boxes[j]))] = d
  return sorted(junction_boxes.items(), key=lambda item: item[1])
  
def part1(path):
    file_data = read_file(path or PATH, return_type=int, strip=True, split=",")
    circuits = []
    junction_boxes = distances(file_data)
    max_connections = 10 if 'test' in path else 1000

    for junction, _ in junction_boxes[:max_connections]:
        box_a, box_b = junction
        found = False
        for circuit in circuits:
            if box_a in circuit and box_b in circuit:
                found = True
                break
            elif box_a in circuit or box_b in circuit:
                circuit.update([box_a, box_b])
                for other in circuits[:]:
                    if other is not circuit and (box_a in other or box_b in other):
                        circuit.update(other)
                        circuits.remove(other)
                found = True
                break
        if not found:
            circuits.append(set([box_a, box_b]))

    return prod(sorted([len(c) for c in circuits], reverse=True)[:3])

def part2(path):
    file_data = read_file(path or PATH, return_type=int, strip=True, split=",")
    circuits = []
    junction_boxes = distances(file_data)

    largest_circuit = 0
    target = None

    for junction, _ in junction_boxes:
        box_a, box_b = junction
        found = False
        for circuit in circuits:
            if box_a in circuit and box_b in circuit:
                found = True
                break
            elif box_a in circuit or box_b in circuit:
                circuit.update([box_a, box_b])
                for other in circuits[:]:
                    if other is not circuit and (box_a in other or box_b in other):
                        circuit.update(other)
                        circuits.remove(other)
                largest_circuit = max(largest_circuit, len(circuit))
                found = True
                break
        if not found:
            circuits.append(set([box_a, box_b]))
            largest_circuit = max(largest_circuit, 2)

        if largest_circuit >= len(file_data):
            target = box_a[0] * box_b[0]
            break
    return target


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")