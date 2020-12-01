from reused import arguments, read_file

PATH="2020/day01/input.txt"
MATCH_NUMBER = 2020

def check_sum(a,b,value):
  if (a + b == value):
    return 0
  elif (a + b > value):
    return 1
  elif (a + b < value):
    return -1

def find_pair(array,value, start=0):
  # print(f'Finding Pair: {value}')
  i = start; j = len(array)-1

  while(True):
    result = check_sum(array[i],array[j],value)
    # print(int(result),array[i],array[j])
    if (result == -1):
      i+=1
    elif (result == 1):
      j-=1
    elif (result == 0):
      return (array[i],array[j])

    if (i == j):
      return (-1,-1)

def part1(path):
  budget_report = read_file(path or PATH,return_type=int,strip=True)
  budget_report.sort()
  # print(budget_report)

  (i,j) = find_pair(budget_report,MATCH_NUMBER)

  print(i,j,i*j)
  pass

def find_triplet(array, value):
  for i in range(len(array)):
    (j,k) = find_pair(array, value-array[i],start=i+1)
    if (j != -1 and k != -1):
      i = array[i]
      return (i,j,k)

def part2(path):
  budget_report = read_file(path or PATH,return_type=int,strip=True)
  budget_report.sort()
  # print(budget_report)

  (i,j,k) = find_triplet(budget_report, MATCH_NUMBER)

  print(i,j,k,i+j+k,i*j*k)
  pass


if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")