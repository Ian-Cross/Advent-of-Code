def get_last_three(arr):
  a = b = c = None
  try:
    a = int(arr[-1])
    b = int(arr[-2])
    c = int(arr[-3])
  except:
    pass
  return a,b,c


def to_num(words: str):
  """ Convert a string representation of a number to its numeric representation """

  teens = {
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
  }

  digits = {
    "zero":0,
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
  }

  tens = {
    "twenty":2,
    "thirty":3,
    "fourty":4,
    "fifty":5,
    "sixty":6,
    "seventy":7,
    "eighty":8,
    "ninty":9,
  }

  scalers = [
    "hundred",
    "thousand",
    "million",
    "billion",
    "trillion",
  ]

  buffer = []
  triplets = []
  scaler_idx = 0
  for word in words.strip().split(" "):
    if word in scalers[1:]:
      if scaler_idx == 0:
        scaler_idx = scalers.index(word)
      else:
        if scaler_idx - scalers.index(word) != 1:
          for _ in range(scaler_idx - scalers.index(word) - 1):
            triplets.append(["zero","hundred"])
            scaler_idx -= 1
        scaler_idx = scalers.index(word)
      triplets.append(buffer)
      buffer = []
      continue
    buffer.append(word)
  if scaler_idx != 1:
    while scaler_idx != 1:
      triplets.append(["zero","hundred"])
      scaler_idx -= 1
  triplets.append(buffer)

  # print(triplets)
  
  num = []
  scaler_idx = len(triplets)-1
  for triple in triplets:
    i = 0
    k = len(triple)
    subnum = []
    while i < len(triple):
      word = triple[i]
      if word == 'zero':
        break

      if word in digits:
        if i+1 < k and triple[i+1] == "hundred":
          
          subnum.append(digits[word]*100)
          i += 1
          continue
        else:
          subnum.append(digits[word])

      
      if word in tens:
        subnum.append(tens[word]*10)
      
      if word in teens:
        subnum.append(teens[word])
      i += 1

    num.append(f"%03d" % sum(subnum))
  
  return int("".join(num))