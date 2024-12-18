day?=$(shell date +%d)
year?=$(shell date +%Y)

all:
	@echo "Welcome to the Advent of Code for ${year}!"
	@echo "Enjoy looking around and think about joining next year!"
	@echo "https://adventofcode.com/"
	

advent:
	pipenv run python3 -m reused.devLoop ${year} ${day}

setup:
	pipenv run python3 -m reused.setup.setup ${year} ${day}