from os import PRIO_USER
from reused import arguments, read_file

PATH = "2021/day08/input.txt"

digit_counts = [6,2,5,5,4,5,6,3,7,5]
special_digits = [2,3,4,7]

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  

  count = 0
  for data in file_data:
    (encoded, display) = data.split('|')

    digits = [digit.replace('*','') for digit in display.strip().split(' ')]
    for digit in digits:
      if len(digit) in special_digits:
        count += 1

  print(count)

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)

  count = 0
  total = 0
  for data in file_data:
    (encoded, display) = data.split('|')

    encoded = encoded.strip().split(" ")
    # for digit in digits:
    decoded = {}
    for i in range(len(encoded)):
      side = [c for c in encoded[i]]
      if (len(side) == 2):
        decoded['1'] = side
        encoded[i] = None
      if (len(side) == 3):
        decoded['7'] = side
        encoded[i] = None
      if (len(side) == 4):
        decoded['4'] = side
        encoded[i] = None
      if (len(side) == 7):
        decoded['8'] = side
        encoded[i] = None
    encoded = list(filter(lambda _: _ is not None, encoded))
    
    # Identified numbers : 1,4,7,8

    mappings = {}
    # Find Mapping: a
    mappings['a'] = list(filter(lambda _: _ not in decoded['1'], decoded['7']))


    # Identified numbers : 1,4,7,8
    # Identified Mappings: a

    # Find number: 5
    _ = list(filter(lambda _: _ not in decoded['1'], decoded['4']))
    print(_)
    for i in range(len(encoded)):
      side = [c for c in encoded[i]]
      if len(side) == 5 and set(_).issubset(side):
        decoded['5'] = side
        encoded[i] = None
        break
    encoded = list(filter(lambda _: _ is not None, encoded))

    # Identified numbers : 1,4,7,8,5
    # Identified Mappings: a

    # Find Mapping: f & c
    mappings['f'] = list(filter(lambda _: _ in decoded['1'], decoded['5']))
    mappings['c'] = list(filter(lambda _: _ not in mappings['f'], decoded['1']))

    potential_e = list(filter(lambda _: _ not in decoded['5'], decoded['8']))
    mappings['e'] = list(filter(lambda _: _ not in mappings['c'], potential_e))

    potential_g = list(filter(lambda _: _ not in decoded['4'], decoded['8']))
    mappings['g'] = list(filter(lambda _: _ not in [mappings['e'][0],mappings['a'][0]], potential_g))

    for i in range(len(encoded)):
      side = [c for c in encoded[i]]
      if len(side) == 6:
        potential_0 = list(filter(lambda _: _ not in [mappings[map][0] for map in mappings], side))
        if len(potential_0) == 1:
          mappings['b'] = potential_0
          decoded['0'] = side
          encoded[i] = None
          break
    encoded = list(filter(lambda _: _ is not None, encoded))
    mappings['d'] = list(filter(lambda _: _ not in decoded['0'], decoded['8']))

    _2 = ['a','c','d','e','g']
    __2 = [mappings[_][0] for _ in _2]
    __2.sort()
    _3 = ['a','c','d','f','g']
    __3 = [mappings[_][0] for _ in _3]
    __3.sort()
    _6 = ['a','b','d','e','f','g']
    __6 = [mappings[_][0] for _ in _6]
    __6.sort()
    _9 = ['a','b','c','d','f','g']
    __9 = [mappings[_][0] for _ in _9]
    __9.sort()

    # print(__2)
    for num in encoded:
      side = [c for c in num]
      side.sort()
      if side == __2:
        decoded['2'] = side
      if side == __3:
        decoded['3'] = side
      if side == __6:
        decoded['6'] = side
      if side == __9:
        decoded['9'] = side


    # print("Decoded Nums: ")
    # for num in decoded:
    #   decoded[num].sort()
    #   print(num, decoded[num])
    # print()


    # print("Side Mappings:")
    # for map in mappings:
    #   print(map, mappings[map])
    # print()

    number = ''
    for digits in display.split(" "):
      num = [_ for _ in digits.strip().replace("*","")]
      num.sort()
      if len(num) == 0:
        continue
      for _ in decoded:
        decoded[_].sort()
        if decoded[_] == num:
          number += _
    total += int(number)
  print(total)


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")