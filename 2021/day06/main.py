from reused import arguments, read_file

PATH = "2021/day06/test.txt"

class Fish:
  def __init__(self,age):
    self.age = age

  def grow(self):
    if (self.age == 0):
      self.age = 6;
      return True
    self.age -= 1
    return False

  def __str__(self):
    return str(self.age)

def print_fishes(fishes):
  for fish in fishes:
    print(fish,end=" ")
  print()

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)

  fishes = [Fish(int(fish)) for fish in file_data[0].split(',')]

  for _ in range(80):
    for fish in fishes:
      did_cycle = fish.grow()
      if (did_cycle):
        fishes.append(Fish(9))

  return(len(fishes))

    
def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  fishes_ints = [int(fish) for fish in file_data[0].split(',')]

  fishes = [0] * 9
  for fish in fishes_ints:
    fishes[fish] += 1

  for _ in range(256):
    fishes = fishes[1:] + fishes[:1]
    fishes[6] += fishes[-1]

  return(sum(fishes))

if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")