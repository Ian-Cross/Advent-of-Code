from reused import arguments, read_file
import string

PATH="2020/day06/input.txt"

def count_unique_letters(arr):
  letter_flags = [0]*26

  for letter in "".join(arr):
    letter_flags[ord(letter)-97] = 1

  return sum(letter_flags)

def count_repeated_letters(arr):
  group = []
  for form in arr:
    letter_flags = ["0"]*26
    for letter in form:
      letter_flags[ord(letter)-97] = "1"
    group.append("".join(letter_flags))
  
  mask = "1"*26
  for form in group:
    mask = [chr(ord(a) & ord(b)) for a,b in zip(mask, form)]

  return sum([int(letter) for letter in mask])



def part1(path):
  customs_forms = read_file(path or PATH,return_type=str,strip=True)

  counts = []
  buffer = []
  for form in customs_forms:
    if (form == ""):
      counts.append(count_unique_letters(buffer))
      buffer = []
    else:
      buffer.append(form)
  counts.append(count_unique_letters(buffer))

  print(sum(counts))

def part2(path):
  customs_forms = read_file(path or PATH,return_type=str,strip=True)

  counts = []
  buffer = []
  for form in customs_forms:
    if (form == ""):
      counts.append(count_repeated_letters(buffer))
      buffer = []
    else:
      buffer.append(form)
  counts.append(count_repeated_letters(buffer))

  print(sum(counts))

if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")