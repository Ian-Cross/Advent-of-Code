from os import curdir
from typing import final
from reused import arguments, read_file

PATH = "2021/day04/test.txt"

class Board:
  def __init__(self):
    self.board = []
    self.won = False

  def array_to_dict(self,row):
    new_row = []
    for num in row:
      if (int(num) < 10):
        num = " " + num
      new_row.append({
        'num': num,
        'marked': False,
      })
    return new_row

  def display(self):
    for x in self.board:
      for y in x:
        if y["marked"]:
          print(f"*{y['num']}*", end=' ')
        else:
          print(f" {y['num']} ", end=' ')
      print()

  def addLine(self, new_line):
    self.board.append(self.array_to_dict(new_line))

  def sum_unmarked(self):
    total = 0
    for x in self.board:
      for y in x:
        if y["marked"] == False:
          total += int(y["num"])
    return total

  def mark_num(self,called):
    for x in self.board:
      for y in x:
        if y["num"].strip() == called:
          y["marked"] = True
          return

  def check_win(self):
    # Check Rows
    for x in self.board:
      no_win = False
      for y in x:
        if not y["marked"]:
          no_win = True
          break
      if (not no_win):
        return True

    # Check Cols
    for i in range(len(self.board[0])):
      no_win = False
      for x in self.board:
        if not x[i]["marked"]:
          no_win = True
          break
      if (not no_win):
        return True

    return False

def play(pull_order,boards):
  for called in pull_order:
    for board in boards:
      board.mark_num(called)
      if (board.check_win()):
        return (called,board)
      
  return (0,0)

def play_to_lose(pull_order,boards):
  for called in pull_order:
    losing_boards = []
    for board in boards:
      if not board.won:
        losing_boards.append(board)

    for board in losing_boards:
      board.mark_num(called)
      if (board.check_win()):
        board.won = True
        if (len(losing_boards) == 1):
          return (called,losing_boards[0])
      
  return (0,0)

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  boards = []
  pull_order = file_data[0].split(",")

  curr_board = Board()
  for line in file_data[2:]:
    if line == "":
      boards.append(curr_board)
      curr_board = Board()
    else:
      to_add = []
      for x in line.strip().split(" "):
        if x != "":
          to_add.append(x)
      curr_board.addLine(to_add)
  boards.append(curr_board)

  final_pull,winning_board = play(pull_order,boards)

  return winning_board.sum_unmarked() * int(final_pull)

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True)
  
  boards = []
  pull_order = file_data[0].split(",")

  curr_board = Board()
  for line in file_data[2:]:
    if line == "":
      boards.append(curr_board)
      curr_board = Board()
    else:
      to_add = []
      for x in line.strip().split(" "):
        if x != "":
          to_add.append(x)
      curr_board.addLine(to_add)
  boards.append(curr_board)

  final_pull,winning_board = play_to_lose(pull_order,boards)

  return winning_board.sum_unmarked() * int(final_pull)


if __name__ == "__main__":
  print(arguments(part1, part2))
  print("\n")