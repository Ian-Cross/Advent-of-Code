import os
import sys
import re
import requests
from markdownify import markdownify
from bs4 import BeautifulSoup

YEAR = 0
DAY = 0


def fetch_input(year, day):
    session = os.environ['session']
    response = requests.get(
        f'https://adventofcode.com/{year}/day/{int(day)}/input',
        headers={"cookie": f"session={session};"}
    )
    return(response.text)


def fetch_story(year, day):
    session = os.environ['session']
    response = requests.get(
        f"https://adventofcode.com/{year}/day/{int(day)}",
        headers={"cookie": f"session={session};"}
    )
    return(response.text)


def extract_story(content):
    soup_aisle = BeautifulSoup(content, features="lxml")
    soup_cans = soup_aisle.find_all("article")

    html_soup = []
    for can in soup_cans:
        title = can.find_all("h2")[0].text
        title = re.sub(" ?--- ?", "", title)
        can.h2.decompose()
        if ("Day" in title):
            html_soup.append(f"<h1>Advent of Code {title}</h1>")
            html_soup.append("<h2>Part 1</h2>")
        else:
            html_soup.append("<h2>Part 2</h2>")
        html_soup.append(str(can))

    opened_soup = "".join(html_soup)
    return markdownify(opened_soup)


def extract_test_case(content):
    soup_aisle = BeautifulSoup(content, features="lxml")
    soup_cans = soup_aisle.find_all("pre")[0]("code")
    opened_soup = ""
    for can in soup_cans:
        opened_soup = can.text
    return opened_soup


def extract_test_answer(content, part):
    soup_aisle = BeautifulSoup(content, features="lxml")
    code_blocks = soup_aisle.find_all('article')[int(part)-1].find_all("code")

    for code_idx in range(len(code_blocks)-1, -1, -1):
        pre_blocks = code_blocks[code_idx].find_all('em')
        if (len(pre_blocks) > 0):
            return pre_blocks[0].text


def make_startup_file(path):
    os.mkdir(path)
    data = None
    template_path = os.getcwd() + "/reused/setup/template.txt"
    with open(template_path, "r") as file:
        data = file.read()

    input_file_path = "/".join(path.split("/")[-2:])
    data = re.sub("INSERT_FILE_PATH", f'"{input_file_path}/test.txt"', data)

    with open(path + "/main.py", "w") as file:
        file.write(data)


def make_day_files(year, day):
    if year not in os.listdir():
        os.mkdir(year)
    else:
        print("Already have year directory")

    file_path = os.getcwd() + "/" + year
    if "day"+day not in os.listdir(file_path):
        make_startup_file(file_path + "/day" + day)
    else:
        print("Already have day directory")


def make_readme(year, day):
    try:
        os.environ['session']
    except KeyError:
        load_env("./reused/.env")

    content = fetch_story(year, day)
    markdown = extract_story(content)
    with open(f"{year}/day{day}/README.md", "w") as output:
        output.write(markdown)


def make_input(year, day):
    file_path = f'{os.getcwd()}/{year}/day{day}'
    if "input.txt" not in os.listdir(file_path):
        input_text = fetch_input(year, day)
        with open(f"{year}/day{day}/input.txt", "w") as output:
            output.write(input_text)
    else:
        print("Already have input file")


def make_test(year, day):
    file_path = f'{os.getcwd()}/{year}/day{day}'
    if "test.txt" not in os.listdir(file_path):
        content = fetch_story(year, day)
        test_case = extract_test_case(content)
        with open(f"{year}/day{day}/test.txt", "w") as output:
            output.write(test_case)
    else:
        print("Already have testing file")


def get_test_answer(year, day, part):
    try:
        os.environ['session']
    except KeyError:
        load_env("./reused/.env")

    content = fetch_story(year, day)
    return extract_test_answer(content, part)


def load_env(path):
    with open(path, "r") as env_file:
        data = env_file.readlines()
        for line in data:
            envs = line.split("=")
            os.environ[envs[0]] = envs[1].strip()


def setup(year, day):
    load_env("./reused/.env")
    make_day_files(year or YEAR, day or DAY)
    make_input(year or YEAR, day or DAY)
    make_test(year or YEAR, day or DAY)
    make_readme(year or YEAR, day or DAY)


if __name__ == "__main__":
    YEAR = sys.argv[1]
    DAY = sys.argv[2]
    setup()
