package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Meta struct {
	min      int
	max      int
	char     string
	password string
}

func make_meta(line string) Meta {
	policy_and_password := strings.Split(line, ": ")
	numbers_and_char := strings.Split(policy_and_password[0], " ")
	min_and_max := strings.Split(numbers_and_char[0], "-")
	min, _ := strconv.Atoi(min_and_max[0])
	max, _ := strconv.Atoi(min_and_max[1])
	return Meta{min, max, numbers_and_char[1], policy_and_password[1]}
}

func validator_one(m Meta) bool {
	count := 0
	for _, c := range m.password {
		if string(c) == m.char {
			count++
		}
	}
	return m.min <= count && count <= m.max
}

func validator_two(m Meta) bool {
	return ((string(m.password[m.min - 1]) == m.char && string(m.password[m.max - 1]) != m.char) ||
		(string(m.password[m.min - 1]) != m.char && string(m.password[m.max - 1]) == m.char))
}

func main() {
	total1 := 0
	total2 := 0
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		m := make_meta(scanner.Text())
		if validator_one(m) {
			total1++
		}
		if validator_two(m) {
			total2++
		}
	}
	fmt.Println("Part 1:", total1)
	fmt.Println("Part 2:", total2)
}
