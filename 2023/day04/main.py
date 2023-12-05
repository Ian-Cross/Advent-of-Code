from reused import arguments, read_file
from collections import defaultdict

PATH = "2023/day04/test.txt"

def build_card(arr):
  while True:
    arr.pop(0)
    if (arr[0] != ""):
      break

  card = {
    'id': int(arr[0][:-1]),
    'win': [],
    'nums': [],
    'points': 0
  }

  target = 'win'
  while True:
    arr.pop(0)
    if len(arr) == 0:
      break
    num = arr[0]

    if num == "|":
      target = 'nums'
    if num == "":
      continue
    card[target].append(num)

  return card

def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, split=" ")
  
  cards = []
  for line in file_data:
    cards.append(build_card(line))

  sum = 0
  for card in cards:
    for num in card['nums']:
      if num in card['win']:
        if card['points'] == 0:
          card['points'] = 1
        else:
          card['points'] *= 2
    sum += card['points']


  return sum

def part2(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, split=" ")
  

  cards = defaultdict(lambda: [])
  for line in file_data:
    card = build_card(line)
    cards[card['id']].append(card)

  for card in cards:
    for copy in cards[card]:
      card_pointer = copy['id'] + 1
      for num in copy['nums']:
        if num in copy['win']:
          cards[card_pointer].append(cards[card_pointer][0])
          card_pointer += 1

  count = 0
  for card in cards:
    count += len(cards[card])

  return count


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")