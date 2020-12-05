from reused import arguments, read_file
import sys

PATH="2020/day05/input.txt"
ROWS=list(range(0,128))
COLS=list(range(0,8))
FRONT="F"
BACK="B"
LEFT="L"
RIGHT="R"

def find_index(str,arr,lower,upper):
  if (len(str) == 0):
    if (len(arr) != 1):
      print("Something has gone wrong finding the row or col")
      sys.exit()
    return arr[0]

  half = int(len(arr)/2)
  if (str[0] == lower):
    return find_index(str[1:],arr[:half],lower,upper)
  elif (str[0] == upper):
    return find_index(str[1:],arr[half:],lower,upper)

def retrieve_id(boarding_pass_str):
  row = find_index(boarding_pass_str[:-3],ROWS,FRONT,BACK)
  col = find_index(boarding_pass_str[7:],COLS,LEFT,RIGHT)
  return row * 8 + col

def part1(path):
  boarding_passes = read_file(path or PATH,return_type=str,strip=True)

  _ids = []
  for boarding_pass in boarding_passes:
    _ids.append(retrieve_id(boarding_pass))

  print(max(_ids))

def part2(path):
  boarding_passes = read_file(path or PATH,return_type=str,strip=True)

  _ids = []
  for boarding_pass in boarding_passes:
    _ids.append(retrieve_id(boarding_pass))
  
  lower_bound = min(_ids)
  upper_bound = max(_ids)

  my_seat = sum(list(range(lower_bound,upper_bound+1))) - sum(_ids)
  print(my_seat)

if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")