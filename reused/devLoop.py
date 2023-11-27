import sys
import os
import inspect
from importlib import import_module, reload

from bs4 import BeautifulSoup
import requests

from reused.setup.setup import setup, get_test_answer, make_readme

year = 0
day = 0


def submit(part, answer):
    print(f"Submiting {answer} to part {part}")
    session = os.environ["session"]
    response = requests.post(
        f'https://adventofcode.com/{year}/day/{int(day)}/answer',
        data={'level': part, 'answer': answer},
        headers={"cookie": f"session={session};"},
    )

    soup_aisle = BeautifulSoup(response.text, features="lxml")
    soup_cans = soup_aisle.find_all('article')
    for can in soup_cans:
        resp = can.text.split(".")[0]
        if ("That's the right answer!" in resp):
            return True
    return False


def testSolution(part, year, day, test_answer=None):
    if test_answer == None:
        test_answer = get_test_answer(year, day, part)

    pyday = import_module(f"{year}.day{day}.main")
    pyday = reload(pyday)

    calculated_answer = getattr(pyday, f"part{part}")(
        f"{year}/day{day}/test.txt")

    if (str(calculated_answer) == str(test_answer)):
        print("Test passed")

        if (submit(part, getattr(pyday, f"part{part}")(f"{year}/day{day}/input.txt"))):
            print("Submission Successful, moving on")
            return True
        else:
            print("Submission failed, take a closer look.")
            return False
    else:
        print(
            f"Test failed, expected {test_answer}, got {calculated_answer}")
        return False


def execute(part, year, day, path):
    pyday = import_module(f"{year}.day{day}.main")
    pyday = reload(pyday)

    if path == None:
        path = 'test'

    print(getattr(pyday, f"part{part}")(
        f"{year}/day{day}/{path}.txt"))


def debug(file=None, function=None, params=None):
    print(params)
    fn = import_module(file)
    fn = reload(fn)
    print(getattr(fn, function)(*params))


def develop(part):
    keys = ['.']
    while (keys[0].lower() != 'q'):
        keys = input(f"[P{part}] Enter command: ").split(" ") + [None]
        try:
            if keys[0] == "s":
                setup(year, day)
            elif keys[0] == "t":
                if testSolution(part, year, day, *keys[1:]):
                    break
            elif keys[0] == 'i':
                if execute(part, year, day, keys[1]):
                    break
            elif keys[0] == 'd':
                debug(keys[1], keys[2], keys[3:])
            elif keys[0] == 'q':
                print("skipping")

        except Exception as e:
            print("Errored out")
            print(e)


def main(y, d):
    global year, day
    year = y
    day = d

    develop(1)
    develop(2)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
