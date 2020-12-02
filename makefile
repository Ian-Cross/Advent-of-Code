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