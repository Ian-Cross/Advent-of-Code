
def get_last_three(arr):
  a = b = c = None
  try:
    a = int(arr[-1])
    b = int(arr[-2])
    c = int(arr[-3])
  except:
    pass
  return a,b,c


def to_word(num: int):
  """ Convert a integer representation of a number to its word representation """

  teens = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
  }

  digits = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
  }

  tens = {
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninty",
  }

  scalers = [
    "hundred",
    "thousand",
    "million",
    "billion",
    "trillion",
  ]

  buffer = str(num)
  words = ""
  scaler_idx = 0
  subset = ""
  while len(buffer) > 0:
    [d1,d2,d3] = get_last_three(buffer)
    subset = ""

    if d1 is not None:
      if d2 != 1 and d1 != 0:
        subset = digits[d1] + " " + subset
    else:
      pass

    if d2 is not None:
      if d2 != 0:
        if d2 == 1:
          subset = teens[int(str(d2) + str(d1))] + " " + subset
        else:
          subset = tens[d2] + " " + subset
    else:
      pass

    if d3 is not None:
      if d3 != 0:
        subset = digits[d3] + " " + scalers[0] + " " + subset
    else:
      pass

    if scaler_idx > 0:
        if not (d1 == 0 and d2 == 0 and d3 == 0):
          subset += scalers[scaler_idx] + " "

    words = subset + words
    scaler_idx+=1
    buffer = buffer[:-3]
  return words