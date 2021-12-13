day?=$(shell date +%d)
year?=$(shell date +%Y)

all:
	@echo "Welcome to the Advent of Code for 2021!"
	@echo "You will find commands to run each day individually,"
	@echo "enjoy looking around and think about joining next year!"

advent:
	python3 -m reused.devLoop ${year} ${day}

setup:
	python3 -m reused.setup.setup ${year} ${day}

day1:
	python3 -m 2021.day01.depths part1
	python3 -m 2021.day01.depths part2

day2:
	python3 -m 2021.day02.main part1
	python3 -m 2021.day02.main part2

day3:
	python3 -m 2021.day03.main part1
	python3 -m 2021.day03.main part2

day4:
	python3 -m 2021.day04.main part1
	python3 -m 2021.day04.main part2

day5:
	python3 -m 2021.day05.main part1
	python3 -m 2021.day05.main part2

day6:
	python3 -m 2021.day06.main part1
	python3 -m 2021.day06.main part2

day7:
	python3 -m 2021.day07.main part1
	python3 -m 2021.day07.main part2

day8:
	python3 -m 2021.day08.main part1
	python3 -m 2021.day08.main part2

day9:
	python3 -m 2021.day09.main part1
	python3 -m 2021.day09.main part2

day10:
	python3 -m 2021.day10.main part1
	python3 -m 2021.day10.main part2

day11:
	python3 -m 2021.day11.main part1
	python3 -m 2021.day11.main part2

day12:
	python3 -m 2021.day12.main part2

day13:
	python3 -m 2021.day13.main part2