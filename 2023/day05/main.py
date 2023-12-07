from reused import arguments, read_file

PATH = "2023/day05/test.txt"

class Map:
  def __init__(self,S):
    lines = S.split("\n")
    self.id = lines.pop(0).split(" ")[0]
    self.tuples: list(tuple[int,int,int]) = tuple([[int(x) for x in line.split(" ")] for line in lines])

  def apply_once(self,x: tuple[int,int,int]) -> int:
    for dest,src,sz in self.tuples:
      if src <= x < src + sz:
        return dest + x - src
    return x

  def apply_range(self, seed_ranges: list[tuple[int,int]]) -> list[tuple[int,int]]:
    range_queue = seed_ranges
    matching_seed_ranges = []

    for (map_dest_start, map_src_start, map_range_size) in self.tuples:
      map_src_end = map_src_start + map_range_size

      new_seed_ranges = []
      while range_queue:
        (range_start,range_end) = range_queue.pop()

        # Define 3 sets, split the seeds according to the map range
        before_range = (range_start,min(range_end,map_src_start))
        in_range = (max(range_start,map_src_start),min(map_src_end,range_end))
        after_range = (max(map_src_end,range_start),range_end)

        # If the sets are non empty, there must be seeds in it, so add it back to the queue and keep processing
        if before_range[1] > before_range[0]:
          new_seed_ranges.append(before_range)
        if after_range[1] > after_range[0]:
          new_seed_ranges.append(after_range)

        # If the seed range and the map range sets overlap, transform according to the map and save
        if in_range[1] > in_range[0]:
          matching_seed_ranges.append((in_range[0] - map_src_start + map_dest_start, in_range[1] - map_src_start + map_dest_start))
      range_queue = new_seed_ranges
    
    return range_queue + matching_seed_ranges


def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, as_one=True, split="\n\n")
  
  seeds = [int(_) for _ in file_data.pop(0).split(" ")[1:]]
  maps = []

  for line in file_data:
    maps.append(Map(line))

  locations = []
  for seed in seeds:
    location = seed
    for map in maps:
      location = map.apply_once(location)
    locations.append(location)
  return min(locations)


def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, as_one=True, split="\n\n")
  
  seeds = [int(_) for _ in file_data.pop(0).split(" ")[1:]]
  seeds = list(zip(seeds[::2],seeds[1::2])) # group the seeds into pairs
  
  maps = []
  for line in file_data:
    maps.append(Map(line))

  locations = []
  for seed in seeds:
    seed_ranges = [(seed[0],sum(seed))]
    
    for map in maps:
      seed_ranges = map.apply_range(seed_ranges)
    locations.append(min(seed_ranges)[0])
  return min(locations)


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")