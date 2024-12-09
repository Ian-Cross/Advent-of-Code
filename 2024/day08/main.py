from reused import arguments, read_file
from common.grid import Grid
from collections import defaultdict
from common.tuples.addTuples import add_tup
from common.tuples.subTuples import sub_tup
from itertools import combinations as combos

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

  def find_antinodes(ant_a, ant_b):
    dy, dx = sub_tup(ant_a, ant_b)

    for antinode in [add_tup(ant_a, (dy, dx)), add_tup(ant_b, (-dy, -dx))]:
      if antenna_map.in_bounds(antinode):
        antinodes.add(antinode)

  for key in antennas:
    for antenna_pair in combos(antennas[key],2):
      find_antinodes(*antenna_pair)

  return len(antinodes)


def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  antenna_map = Grid()
  antenna_map.fill(file_data,callback=find_antennas)
  antinodes = set()

  for key in antennas:
    for i in range(len(antennas[key])):
      for j in range(i + 1, len(antennas[key])):
        dy, dx = sub_tup(antennas[key][i],antennas[key][j])

        antinode_a = antennas[key][i]
        while antenna_map.in_bounds(antinode_a):
          antinodes.add(antinode_a)
          antinode_a = add_tup(antinode_a,(dy,dx))
        
        antinode_b = antennas[key][j]
        while antenna_map.in_bounds(antinode_b):
          antinodes.add(antinode_b)
          antinode_b = add_tup(antinode_b,(-dy,-dx))

  return len(antinodes)


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")