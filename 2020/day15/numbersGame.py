from reused import arguments, read_file

PATH="2020/day15/input.txt"

def last_index_of (list,num):
  index = -1

  for i in range(len(list[:-1])-1,-1,-1):
    if (list[i] == num):
      index = i
      break

  return index

def get_last_num (list):
  return list[-1]

def part1(path):
  starting_numbers = read_file(path or PATH,return_type=int,strip=True,split=",")[0]
  num_turns = 2020

  numbers = starting_numbers
  i = len(numbers)+1
  while (i <= num_turns):
    last_num = get_last_num(numbers)
    last_index = last_index_of(numbers,last_num)
    if (last_index == -1):
      numbers.append(0)
    else:
      numbers.append(len(numbers) - (last_index+1))
    i += 1
  print(numbers[-1])

def part2(path):
  numbers = read_file(path or PATH,return_type=int,strip=True,split=",")[0]
  num_turns = 30000000

  # A "memory" to store the past idices of values for quick lookup
  last_occurance = [0] * num_turns
  
  # Take the first few turns
  for turn, num in enumerate(numbers[:-1], 1):
    last_occurance[num] = turn
  
  last_num = numbers[-1]
  # interate through all the pages
  for turn_number in range(len(numbers), num_turns):
    # last time the number was said
    last_seen = last_occurance[last_num]
    # Distance from current number said
    num_age = turn_number - last_seen
    # First time number has been said
    if num_age == turn_number:
      num_age = 0
    # load current number into memory
    last_occurance[last_num] = turn_number
    last_num = num_age
    
  print(num_age)

if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")