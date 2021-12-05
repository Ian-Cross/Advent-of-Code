import sys, os
from reused.setup.setup import setup, get_test_answer, make_readme
import subprocess
from importlib import import_module, reload
import requests
from bs4 import BeautifulSoup

year = 0
day = 0
def submit(part, answer):
  print(f"{answer} to part {part}")
  session = os.environ["session"]
  response = requests.post(
    f'https://adventofcode.com/{year}/day/{int(day)}/answer',
    data={'level': part, 'answer': answer},
    headers={"cookie": f"session={session};"},
  )

  soup_aisle = BeautifulSoup(response.text,features="lxml")
  soup_cans = soup_aisle.find_all('article')
  for can in soup_cans:
    resp = can.text.split(".")[0]
    if ("That's the right answer!" in resp):
      return True
  return False
  

def part_1():
  key = '.'
  pyday = import_module(f"{year}.day{day}.main")
  while (key.lower() != 'q'):
    key = input("Enter command: ")

    if key == "s":
      setup(year,day)
    elif key == "t":
      test_answer = get_test_answer(year,day, 1)

      pyday = reload(pyday)

      calculated_answer = pyday.part1(f"{year}/day{day}/test.txt")

      if (str(calculated_answer) == str(test_answer)):
        print("Test passed, submitting...", end=" ")
        if (submit(1,pyday.part1(f"{year}/day{day}/input.txt"))):
          print("Submission Successful, moving to part 2")
          key = 'q'
        else:
          print("Submission failed, take a closer look.")
      else:
        print(f"Test failed, expected {test_answer}, got {calculated_answer}")


def part_2():
  key = '.'
  pyday = import_module(f"{year}.day{day}.main")
  while (key.lower() != 'q'):
    key = input("Enter command: ")

    if key == "s":
      make_readme(year,day)
    elif key == "t":
      test_answer = get_test_answer(year,day,2)
      pyday = reload(pyday)

      calculated_answer = pyday.part2(f"{year}/day{day}/test.txt")

      if (str(calculated_answer) == str(test_answer)):
        print("Test passed, submitting...")
        if (submit(2,pyday.part2(f"{year}/day{day}/input.txt"))):
          print("Submission Successful! Nice Work")
          key = 'q'
        else:
          print("Submission failed, take a closer look.")
      else:
        print(f"Test failed, expected {test_answer}, got {calculated_answer}")

def main(y,d):
  global year,day
  year = y
  day = d

  part_1()
  part_2()


if __name__ == "__main__":
  main(sys.argv[1],sys.argv[2])