package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func multiply_two_numbers_totaling(val int, list map[int]int) int {
	for v, _ := range list {
		diff := val - v
		_, ok := list[diff]
		if ok {
			return diff * v
		}
	}
	return 0
}

func multiply_three_numbers_totaling(val int, list map[int]int) int {
	for v, _ := range list {
		diff := val - v
		match := multiply_two_numbers_totaling(diff, list)
		if match != 0 {
			return v * match
		}
	}
	return 0
}

func main() {
	f, _ := os.Open("expenses.txt")
	defer f.Close()

	list := make(map[int]int)
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		val, _ := strconv.Atoi(scanner.Text())
		list[val] = 0
	}
	fmt.Println(multiply_two_numbers_totaling(2020, list))
	fmt.Println(multiply_three_numbers_totaling(2020, list))
}
