all:
	@echo "Welcome to the Advent of Code for 2020!"
	@echo "You will find commands to run each day individually,"
	@echo "enjoy looking around and think about joining next year!"

day01:
	python3 -m 2020.day01.budgetReport part1
	python3 -m 2020.day01.budgetReport part2

day02:
	python3 -m 2020.day02.validPasswords part1
	python3 -m 2020.day02.validPasswords part2

day03:
	python3 -m 2020.day03.treemap part1
	python3 -m 2020.day03.treemap part2

day04:
	python3 -m 2020.day04.passports part1
	python3 -m 2020.day04.passports part2

day05:
	python3 -m 2020.day05.boardingPasses part1
	python3 -m 2020.day05.boardingPasses part2

day06:
	python3 -m 2020.day06.customsForm part1
	python3 -m 2020.day06.customsForm part2

day07:
	python3 -m 2020.day07.luggage part1
	python3 -m 2020.day07.luggage part2

day08:
	python3 -m 2020.day08.gameConsole part1
	python3 -m 2020.day08.gameConsole part2