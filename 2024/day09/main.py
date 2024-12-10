from reused import arguments, read_file
from copy import deepcopy

PATH = "2024/day09/test.txt"

def part1(path):
  file_data = read_file(path or PATH, return_type=int, strip=True, as_one=True, split=r'(\d)', exclude_none=True)
  
  files = []
  file_id = 0
  is_file = True 
  for i in file_data:
    files.extend([file_id if is_file else '.'] * i)
    if is_file:
      file_id += 1
    is_file = not is_file

  read_head = len(files) - 1
  write_head = 0
  while write_head < read_head:
    if files[write_head] == '.':
      while files[read_head] == '.' and read_head > write_head:
        read_head -= 1
      if write_head < read_head:
        files[write_head], files[read_head] = files[read_head], files[write_head]
    write_head += 1

  return sum(files[i] * i for i in range(len(files)) if files[i] != '.')

def part2(path):
  file_data = read_file(path or PATH, return_type=int, strip=True, as_one=True, split=r'(\d)', exclude_none=True)

  details = []
  file_id = 0
  is_file = True 
  for i in file_data:
    details.append({
      'id': file_id if is_file else '.',
      'len': i,
      'is_file': is_file,
      'moved': False
    })
    if is_file:
      file_id += 1
    is_file = not is_file


  i = len(details) - 1
  while i >= 0:
    read_head = details[i]
    if read_head['id'] == '.' or read_head['moved']:
      i -= 1
      continue
    
    j = 0
    while j < i:
      write_head = details[j]
      if write_head['id'] != '.' or write_head['len'] < read_head['len']:
        j += 1
        continue


      temp_read = deepcopy(read_head)
      read_head['id'] = '.'
      read_head['is_file'] = False

      if 0 < i < len(details)-1 and details[i-1]['id'] == '.' and details[i+1]['id'] == '.':
        details[i-1]['len'] += read_head['len'] + details[i+1]['len']
        del details[i+1]
      elif 0 < i < len(details) and details[i-1]['id'] == '.':
        details[i-1]['len'] += read_head['len']
      elif 0 <= i < len(details)-1 and details[i+1]['id'] == '.':
        details[i+1]['len'] += read_head['len']
      del details[i]
      i -= 1

      
      temp_read['moved'] = True
      details.insert(j, temp_read)
      i += 1
      j += 1

      if details[j-1]['id'] != '.' or details[j+1]['id'] != '.':
        details.insert(j, {
          'id': ".",
          'len': 0,
          'is_file': False,
          'moved': False
        })
        i += 1
        j += 1

      write_head['len'] -= temp_read['len']
      if write_head['len'] == 0:
        del details[j]
        i -= 1
      break

    i -= 1

  line = []
  for i in details:
    line.extend([str(i['id']) if i['is_file'] else '.'] * i['len'])

  return sum(int(line[i]) * i for i in range(len(line)) if line[i] != '.')

if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")