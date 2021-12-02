day?=$(shell date +%d)
year?=$(shell date +%Y)

all:
	@echo "Welcome to the Advent of Code for 2021!"
	@echo "You will find commands to run each day individually,"
	@echo "enjoy looking around and think about joining next year!"

setup:
	python3 -m reused.setup.setup ${year} ${day}

day01:
	python3 -m 2021.day01.depths part1
	python3 -m 2021.day01.depths part2