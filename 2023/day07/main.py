from reused import arguments, read_file
from collections import defaultdict, Counter

PATH = "2023/day07/test.txt"

map = { 
  '2': '2',
  '3': '3',
  '4': '4',
  '5': '5',
  '6': '6',
  '7': '7',
  '8': '8',
  '9': '9',
  'T': 'A',
  'J': 'B',
  'Q': 'C',
  'K': 'D',
  'A': 'E',
}

# types = defaultdict(lambda: {})
types = ['High Card',"One Pair",'Two Pair',"Three of a kind", 'Full House', 'Four of a kind', 'Five of a kind']

class Hand:
  def __init__(self,cards,bet):
    self.cards = [map[x] for x in list(cards)]
    self.bet = int(bet)
    self.type = ''

  def display(self):
    print(self.cards)

  def find_type(self):
    card_set = Counter(self.cards)
    self.assign_hand_value(card_set)
    
  def find_type_with_wild(self,wild):

    card_set = Counter(self.cards)

    if map[wild] in card_set:
      wild_count = card_set[map[wild]]
      card_set.pop(map[wild])
      if len(card_set) == 0:
        card_set[map['A']] = wild_count
      else:
        card_set[card_set.most_common(1)[0][0]] += wild_count
    self.assign_hand_value(card_set)
    
  def assign_hand_value(self, cards: Counter):
    if len(cards) == 5:
      self.type = '0'
      return
    if len(cards) == 4:
      self.type = '1'
      return
    if len(cards) == 3:
      self.type = str(cards.most_common(1)[0][1])
      return
    if len(cards) == 2:
      self.type = str(cards.most_common(1)[0][1] + 1)
      return
    if len(cards) == 1:
      self.type = '6'
      return


def part1(path):
  file_data = read_file(path or PATH, return_type=str, strip=True, split=" ")
  
  hands = []
  for line in file_data:
    hands.append(Hand(line[0],line[1]))
    hands[-1].find_type()
  hands.sort(key=lambda x: int(x.type + "".join(x.cards),16), reverse=True)
  
  sum = 0
  for i,hand in enumerate(hands):
    sum += hand.bet * (len(hands) - i)
  return sum

def part2(path):
  global map

  map['J'] = '1'
  file_data = read_file(path or PATH, return_type=str, strip=True, split=" ")
  
  hands = []
  for line in file_data:
    hands.append(Hand(line[0],line[1]))
    hands[-1].find_type_with_wild('J')
  
  hands.sort(key=lambda x: int(x.type + "".join(x.cards),16), reverse=True)

  sum = 0
  for i,hand in enumerate(hands):
    sum += hand.bet * (len(hands) - i)
  return sum


if __name__ == "__main__":
  arguments(part1, part2)
  print("\n")