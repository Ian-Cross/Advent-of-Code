from reused import arguments, read_file

PATH = "2021/day03/test.txt"

def part1(path):
  inputs = read_file(path or PATH, return_type=str, strip=True)
  
  most_common = []
  for bit in inputs[0]:
    most_common.append({
      '0': 0,
      '1': 0,
    })

  for input in inputs:
    for i in range(len(input)):
      most_common[i][input[i]] += 1
  
  gamma_bin = []
  epsilon_bin = []
  for common in most_common:
    if common['0'] > common['1']:
      gamma_bin.append('0')
      epsilon_bin.append('1')
    else:
      gamma_bin.append('1')
      epsilon_bin.append('0')

  gamma_dec = int("".join(gamma_bin),2)
  epsilon_dec = int("".join(epsilon_bin),2)

  print(gamma_dec * epsilon_dec)

def trim(list, idx, matching_bit):
  return_list = []
  for item in list:
    if item[idx] == matching_bit:
      return_list.append(item)
  return return_list

def mcb(list,idx):
  common = {
    '0': 0,
    '1': 0
  }
  for item in list:
    common[item[idx]] += 1
  return common

def part2(path):
  inputs = read_file(path or PATH, return_type=str, strip=True)
  oxygen = inputs
  co2 = inputs
  
  for i in range(len(inputs[0])):
    if (len(oxygen) > 1):
      oxygen_mcb = mcb(oxygen,i)
      if oxygen_mcb['0'] > oxygen_mcb['1']:
        oxygen = trim(oxygen,i,'0')
      else:
        oxygen = trim(oxygen,i,'1')

    if (len(co2) > 1):
      co2_mcb = mcb(co2,i)
      if co2_mcb['0'] > co2_mcb['1']:
        co2 = trim(co2,i,'1')
      else:
        co2 = trim(co2,i,'0')

  oxygen_dec = int(oxygen[0],2)
  co2_dec = int(co2[0],2)
  print(oxygen_dec * co2_dec)


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")