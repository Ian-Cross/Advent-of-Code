from reused import arguments, read_file
import json, sys

PATH="2020/day09/input.txt"
LOOK_BACK = 25

def check_sums(arr,val):
  for x in arr:
    for y in arr:
      if (x == y):
        continue
      if (x + y == val):
        return True
  return False

def find_invalid_number(port_output):
  preamble = []
  invalid = []
  for num in port_output:
    if (len(preamble) < LOOK_BACK):
      preamble.append(num)
      continue
    if (not check_sums(preamble,num)):
      invalid.append(num)
    preamble.pop(0)
    preamble.append(num)
  return invalid

def contiguous_sum(arr,val):
  for i in range(len(arr)):
    contiguous_list = []
    for y in arr[i:]:
      contiguous_list.append(y)
      if (sum(contiguous_list) > val):
        break
      elif (sum(contiguous_list) == val):
        return contiguous_list

def part1(path):
  port_output = read_file(path or PATH,return_type=int,strip=True)
  print(find_invalid_number(port_output))

def part2(path):
  port_output = read_file(path or PATH,return_type=int,strip=True)

  weakness_sum = find_invalid_number(port_output)
  if (len(weakness_sum) > 1):
    print("Something has gone wrong")
    sys.exit()
  weakness_sum = weakness_sum[0]

  contiguous_list = contiguous_sum(port_output,weakness_sum)
  print(min(contiguous_list) + max(contiguous_list))


if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")