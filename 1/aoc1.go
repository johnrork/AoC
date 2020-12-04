package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func contains(s []int, e int) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func multiply_two_numbers_totaling(val int, list []int) int {
	for _, v := range list {
		diff := val - v
		if contains(list, diff) {
			return diff * v
		}
	}
	return 0
}

func multiply_three_numbers_totaling(val int, list []int) int {
	for _, v := range list {
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

	var list []int
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		val, _ := strconv.Atoi(scanner.Text())
		list = append(list, val)
	}
	fmt.Println(multiply_two_numbers_totaling(2020, list))
	fmt.Println(multiply_three_numbers_totaling(2020, list))
}
