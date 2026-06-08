package main

import (
	"bufio"
	"fmt"
	"os"
)

func readInput(path string) []string {
	file, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	data := []string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		data = append(data, line)
	}
	return data
}

func part1(path string) int {
	file_data := readInput(path)

	sum := 0
	for _, line := range file_data {
		adjusted_line := line + string(line[0])
		last_digit := rune(0)
		for _, ch := range adjusted_line {
			if last_digit == 0 {
				last_digit = ch
				continue
			}
			if ch == last_digit {
				digit := int(ch - '0')
				sum += digit
			}
			last_digit = ch
		}
	}
	return sum
}

func part2(path string) int {
	file_data := readInput(path)

	sum := 0
	for _, line := range file_data {
		length := len(line)
		half := length / 2
		for i, ch := range line {
			match := rune(line[(i+half)%length])
			if ch == match {
				sum += int(ch - '0')
			}
		}
	}
	return sum
}

func main() {
	part := os.Args[1]
	path := os.Args[2]
	switch part {
	case "part1":
		fmt.Println(part1(path))
	case "part2":
		fmt.Println(part2(path))
	}
}
