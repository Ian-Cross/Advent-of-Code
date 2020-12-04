from reused import arguments, read_file
import string

PATH="2020/day04/input.txt"
PASSPORT_ELEMENTS = ['ecl','pid','eyr','hcl','byr','iyr','hgt']
EYE_COLOURS = ['amb','blu','brn','gry','grn','hzl','oth']

class Passport:
  def __init__(self,buffer):
    self.build_passport(buffer)

  def build_passport(self,passport):
    for piece in passport:
      components = piece.split(" ")
      for element in components:
        [key,value] = element.split(":")
        setattr(self,key,value)

  def __repr__(self):
    return '<Passport(PID={self.pid!r})>'.format(self=self)

  def data_validation(self):
    keys = self.__dict__.keys()

    for key in PASSPORT_ELEMENTS:
      if (key not in keys):
        return False

    # Height
    hgt_unit = getattr(self,"hgt")[-2:]
    hgt_val = getattr(self,"hgt")[:-2]
    if (hgt_unit != "cm" and hgt_unit != "in"):
      return False

    try:
      # Birth Year
      int_byr = int(getattr(self,"byr"))
      if (int_byr > 2002 or int_byr < 1920):
        return False
      # Issue Year
      int_iyr = int(getattr(self,"iyr"))
      if (int_iyr > 2020 or int_iyr < 2010):
        return False
      # Expiration Year
      int_eyr = int(getattr(self,"eyr"))
      if (int_eyr > 2030 or int_eyr < 2020):
        return False
      # Height
      hgt_val = int(hgt_val)
      if (hgt_unit == "cm" and (hgt_val > 193 or hgt_val < 150)):
        return False
      if (hgt_unit == "in" and (hgt_val > 76 or hgt_val < 59)):
        return False

    except ValueError:
      return False

    # Hair Colour
    if (len(getattr(self,"hcl")[1:]) != 6 or not all(c in string.hexdigits for c in getattr(self,"hcl")[1:])):
      return False

    # Eye Colour
    if (getattr(self,"ecl") not in EYE_COLOURS):
      return False

    # PID
    if (len(getattr(self,"pid")) != 9 or not all(c in string.digits for c in getattr(self,"pid"))):
      return False
    
    return True

  def is_valid(self, validate_data = False):
    keys = self.__dict__.keys()
    if (len(keys) < 7):
      return False
    
    if (len(keys) == 7 and "cid" in keys):
      return False

    if (validate_data and not self.data_validation()):
      return False
    return True

def collect_passports(file_data):
  passports = []
  buffer = []
  for piece in file_data:
    if (piece == ""):
      passports.append(Passport(buffer))
      buffer = []
    else:
      buffer.append(piece)
  passports.append(Passport(buffer))
  return passports


def part1(path):
  file_passports = read_file(path or PATH,return_type=str,strip=True)

  passports = collect_passports(file_passports)

  valid_count = 0
  for passport in passports:
    if (passport.is_valid()):
      valid_count += 1
  print(valid_count)


def part2(path):
  file_passports = read_file(path or PATH,return_type=str,strip=True)

  passports = collect_passports(file_passports)

  valid_count = 0
  for passport in passports:
    if (passport.is_valid(validate_data=True)):
      valid_count += 1
  print(valid_count)

if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")