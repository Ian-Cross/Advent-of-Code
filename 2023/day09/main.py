from reused import arguments, read_file

PATH = "2023/day09/test.txt"

def gen_differences(arr):
  return [(arr[i+1] - arr[i]) for i in range(len(arr)-1)]


def generate_history(arr):
  history = [arr]
  while not all(_ == 0 for _ in history[-1]):
    history.append(gen_differences(history[-1]))
  return history


def part1(path):
  file_data = read_file(path or PATH, return_type=int, strip=True, split=' ')
  
  total = 0
  for line in file_data:
    history = generate_history(line)
    total += sum([x[-1] for x in history])

  return total

def part2(path):
  file_data = read_file(path or PATH, return_type=int, strip=True, split=' ')
  
  total = 0
  for line in file_data:
    history = generate_history(line)
    total += sum([-1*x[0] for x in history][1::2] + [x[0] for x in history][::2])    
  return total


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")