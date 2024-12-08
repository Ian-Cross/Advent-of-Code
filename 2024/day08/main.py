from reused import arguments, read_file
from common.grid import Grid
from collections import defaultdict
from common.tuples.addTuples import add_tup

PATH = "2024/day08/test.txt"
antennas = defaultdict(list)


def find_antennas(_,y,item,x):
  global antennas
  if item.data == ".":
    return
  antennas[item.data].append((y,x))


def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  antenna_map = Grid()
  antenna_map.fill(file_data,callback=find_antennas)
  antinodes = set()

  for key in antennas:
    for i in range(len(antennas[key])):
      for j in range(i+1,len(antennas[key])):

        distance_y = antennas[key][i][0] - antennas[key][j][0]
        distance_x = antennas[key][i][1] - antennas[key][j][1]

        antinode_a = add_tup(antennas[key][i],(distance_y,distance_x))
        antinode_b = add_tup(antennas[key][j],(-distance_y,-distance_x))

        if antenna_map.in_bounds(antinode_a):
          antinodes.add(antinode_a)
        if antenna_map.in_bounds(antinode_b):
          antinodes.add(antinode_b)
  return len(antinodes)


def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  antenna_map = Grid()
  antenna_map.fill(file_data,callback=find_antennas)
  antinodes = set()

  for key in antennas:
    for i in range(len(antennas[key])):
      for j in range(i+1,len(antennas[key])):

        distance_y = antennas[key][i][0] - antennas[key][j][0]
        distance_x = antennas[key][i][1] - antennas[key][j][1]

        antinode_a = antennas[key][i]
        while antenna_map.in_bounds(antinode_a):
          antinodes.add(antinode_a)
          antinode_a = add_tup(antinode_a,(distance_y,distance_x))
        
        antinode_b = antennas[key][j]
        while antenna_map.in_bounds(antinode_b):
          antinodes.add(antinode_b)
          antinode_b = add_tup(antinode_b,(-distance_y,-distance_x))

  return len(antinodes)


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")