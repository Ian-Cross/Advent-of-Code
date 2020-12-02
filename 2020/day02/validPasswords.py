from reused import arguments, read_file

PATH="2020/day02/input.txt"


def parse_password(str):
  parts = str.split(" ")
  parts[0] = parts[0].split("-")
  parts[1] = parts[1].split(":")[0]
  return parts

def valid_password_count(password_spec):
  high_low = password_spec[0]
  constraint = password_spec[1]
  password = password_spec[2]

  occurances = 0
  for char in password:
    if char == constraint:
      occurances+=1

  if (occurances >= int(high_low[0]) and occurances <= int(high_low[1])):
    return True
  return False

def valid_password_xor(password_spec):
  [pos_1,pos_2] = password_spec[0]
  constraint = password_spec[1]
  password = password_spec[2]

  pos_1 = int(pos_1)-1
  pos_2 = int(pos_2)-1

  if (password[pos_1] == constraint and password[pos_1] != password[pos_2]):
    return True
  if (password[pos_2] == constraint and password[pos_1] != password[pos_2]):
    return True
  return False


def part1(path):
  passwords = read_file(path or PATH,return_type=str,strip=True)

  count = 0
  for password in passwords:
    spec = parse_password(password)
    if (valid_password_count(spec)):
      count += 1
  print(count)

def part2(path):
  passwords = read_file(path or PATH,return_type=str,strip=True)

  count = 0
  for password in passwords:
    spec = parse_password(password)
    if (valid_password_xor(spec)):
      count += 1
  print(count)



if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")