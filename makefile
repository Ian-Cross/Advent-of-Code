day?=$(shell date +%d)
year?=$(shell date +%Y)

all:
	@echo "Welcome to the Advent of Code for ${year}!"
	@echo "You will find commands to run each day individually,"
	@echo "enjoy looking around and think about joining next year!"

advent:
	python3 -m reused.devLoop ${year} ${day}

setup:
	python3 -m reused.setup.setup ${year} ${day}