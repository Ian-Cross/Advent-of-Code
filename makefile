all: day1 day2 day3 day4 day5 day6

day1:
	python3 -m 1stDay.fuelCost part1
	python3 -m 1stDay.fuelCost part2

day2:
	python3 -m 2ndDay.intcode part1
	python3 -m 2ndDay.intcode part2

day3:
	python3 -m 3rdDay.manhatten part1
	python3 -m 3rdDay.manhatten part2

day4:
	python3 -m 4thDay.password part1
	python3 -m 4thDay.password part2

day5:
	python3 -m 5thDay.diagnostic part1
	python3 -m 5thDay.diagnostic part2

day6:
	python3 -m 6thDay.orbits part1
	python3 -m 6thDay.orbits part2
