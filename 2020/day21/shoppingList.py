from reused import arguments, read_file

PATH="2020/day21/test.txt"

class Dish():
  def __init__(self,ingredients,alergens):
    self.ingredients = ingredients
    self.alergens = alergens

  def __str__(self):
    return " ".join(self.ingredients) + "\n  " + " ".join(self.alergens)

  def has_alergen(self,alergen):
    if alergen in self.alergens:
      return True
    return False

def part1(path):
  shopping_list = read_file(path or PATH,return_type=str,strip=True)

  dish_list = []
  alergens = []
  ingredients = []
  
  for food in shopping_list:
    (dish_ingredients,dish_alergens) = food.split("(")
    dish_ingredients = dish_ingredients.split(" ")[:-1]
    dish_alergens = dish_alergens.split(")")[0].split(" ")[1:]
    for alergen in dish_alergens:
      if alergen not in alergens:
        alergens.append(alergen)
      
    for ingredient in dish_ingredients:
      if ingredient not in ingredients:
        ingredients.append(ingredient)

    dish_list.append(Dish(dish_ingredients,dish_alergens))

  print(alergens)
  print(ingredients)

  for dish in dish_list:
    print(dish)


def part2(path):
  shopping_list = read_file(path or PATH,return_type=str,strip=True)
  
if __name__ == "__main__":
    arguments(part1,part2)
    print("\n")