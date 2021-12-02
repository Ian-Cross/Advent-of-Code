import sys

def usage():
  """
  Desc: Close the program and inform the user how to properly invoke the programs
  """
  print("To run a specific day and part execute the program as:")
  print("python3 -m 1stDay.adventOfCode part1 datafile[optional]")
  exit(1)


def arguments(part_1=None, part_2=None):
    """
    Desc: Use the program arguments to envoke the proper part of that
    day, including the desired data if needed
    Param: part_1: function pointer to the first part of that day
            part_2: function pointer to the second part of that day
    """
    path = None
    # Use a datafile if provided
    if len(sys.argv) == 3:
        path = sys.argv[2]
        if sys.argv[1] == "part1":
            part_1(path=path)
        elif sys.argv[1] == "part2":
            part_2(path=path)
        else:
            usage()
    # run the desired part of that day
    elif len(sys.argv) == 2:
        if sys.argv[1] == "part1":
            part_1(path=path)
        elif sys.argv[1] == "part2":
            part_2(path=path)
        else:
            usage()
    else:
        usage()
