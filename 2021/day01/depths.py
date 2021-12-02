from reused import arguments, read_file

PATH = "2021/day01/test.txt"

def part1(path):
	depths = read_file(path or PATH, return_type=int, strip=True)
	num_increases = 0

	last_depth = depths[0]
	for i in range(1,len(depths)):
		if (depths[i] > last_depth):
			num_increases += 1
		last_depth = depths[i]
	print(f"Number of increases {num_increases}")

def part2(path):
	depths = read_file(path or PATH, return_type=int, strip=True)

	def get_triple(i):
		return depths[i] + depths[i+1] + depths[i+2]

	num_increases = 0
	last_depth = get_triple(0)

	for i in range(len(depths)-2):
		total = get_triple(i)
		if (total > last_depth):
			num_increases+=1
		last_depth = total
	print(f"Number of increases {num_increases}")


if __name__ == "__main__":
    arguments(part1, part2)
    print("\n")
