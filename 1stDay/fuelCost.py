from reused import arguments, readFile
from math import floor

PATH = "1stDay/input.txt"

"""
Desc: Calculate the extra needed fuel from the weight of each rocket module
Param: file path to a provided datafile
"""
def part_1(path):
    # Colect the weights of the modules
    module_weights = readFile(path or PATH, return_type=int,strip=True)
    # Calculate the fuel cost for each module
    fuel_cost = [floor(weight/3)-2 for weight in module_weights]
    # Provide the summation as the solution
    print(sum(fuel_cost))

"""
Desc: Calculate the extra needed fuel from the weight of each rocket module
      including the added weight from the newly added fuel
Param: file path to a provided datafile
"""
def part_2(path):
    # Colect the weights of the modules
    module_weights = readFile(path or PATH, return_type=int,strip=True)

    """
    Desc: A recursive function used to calculate the weight of modules,
          then the weight of that added fuel and so on until reaching the
          "Wishing really hard" cutoff
    Param: weight: int of the weight to calculate fuel cost for
    """
    def fuel_cost(weight):
        curr_weight = 0
        curr_cost = floor(weight/3)-2
        # Wishing really hard cutoff
        if (curr_cost >= 0):
            # Add the current fuel weight to the total
            curr_weight += curr_cost
            # Calculate the next weight from the newly added fuel
            curr_weight += fuel_cost(curr_cost)
            return curr_weight
        return 0

    # Build an array of each modules total fuel costs
    fuel_cost = [fuel_cost(weight) for weight in module_weights]
    # Provide the summation as the solution
    print(sum(fuel_cost))


if __name__ == '__main__':
    arguments(part_1,part_2)
