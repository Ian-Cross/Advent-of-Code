import os
import sys
import re
import requests
from markdownify import markdownify
from bs4 import BeautifulSoup

def make_startup_file(path,day):
  os.mkdir(path)
  data = None
  template_path = os.getcwd() + "/reused/setup/template.txt"
  with open(template_path,"r") as file:
    data = file.read()

  input_file_path = "/".join(path.split("/")[-2:])
  data = re.sub("INSERT_FILE_PATH",f'"{input_file_path}/test.txt"',data)

  with open(path + "/day" + day + ".py","w") as file:
    file.write(data)


def make_day_files(year,day):
  if year not in os.listdir():
    os.mkdir(year)

  file_path = os.getcwd() + "/" + year
  if "day"+day not in os.listdir(file_path):
    make_startup_file(file_path + "/day" + day,day)

def fetch_story(year, day):
  session = os.environ['session']
  response = requests.get(
    f'https://adventofcode.com/{year}/day/{str(int(day))}',
    headers={
      'authority':'adventofcode.com',
      'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-user': '?1',
      'sec-fetch-dest': 'document',
      'referer': 'https://adventofcode.com/',
      'accept-language': 'en-US,en;q=0.9',
      'cookie': f'_ga=GA1.2.1857611616.1638368842; _gid=GA1.2.1105675078.1638368842; session={session}; _gat=1'
    }
  )
  return(response.text)

def extract_story(content):
  soup_aisle = BeautifulSoup(content)
  soup_cans = soup_aisle.find_all("article")

  html_soup = []
  for can in soup_cans:
    title = can.find_all("h2")[0].text
    title = re.sub(" ?--- ?","",title)
    can.h2.decompose()
    if ("Day" in title):
      html_soup.append(f"<h1>Advent of Code {title}</h1>")
      html_soup.append("<h2>Part 1</h2>")
    else:
      html_soup.append("<h2>Part 2</h2>")
    html_soup.append(str(can))

  opened_soup = "".join(html_soup)
  return markdownify(opened_soup)

def make_readme(year, day):
  content = fetch_story(year, day)
  markdown = extract_story(content)

  with open(f"{year}/day{day}/README.md","w") as output:
    output.write(markdown)


def fetch_input(year,day):
  session = os.environ['session']
  response = requests.get(
    f'https://adventofcode.com/{year}/day/{str(int(day))}/input',
    headers={
      'authority':'adventofcode.com',
      'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-user': '?1',
      'sec-fetch-dest': 'document',
      'referer': 'https://adventofcode.com/',
      'accept-language': 'en-US,en;q=0.9',
      'cookie': f'_ga=GA1.2.1857611616.1638368842; _gid=GA1.2.1105675078.1638368842; session={session}; _gat=1'
    }
  )
  return(response.text)

def make_input(year,day):
  input_text = fetch_input(year,day)
  with open(f"{year}/day{day}/input.txt","w") as output:
    output.write(input_text)


def load_env(path):
  with open(path,"r") as env_file:
    data = env_file.readlines()
    for line in data:
      envs = line.split("=")
      os.environ[envs[0]] = envs[1]

def main(year, day):
  load_env("./reused/.env")
  make_day_files(year, day)
  make_readme(year, day)
  make_input(year,day)
  

if __name__ == "__main__":
  main(sys.argv[1],sys.argv[2])