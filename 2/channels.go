package main
import (
	"os"
	"fmt"
	"bufio"
	"strings"
	"strconv"
)

type Meta struct {
	min int
	max int
	char string
	password string
}

type validator func(Meta) bool

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
	for _, c := range(m.password) {
		if (string(c) == m.char){
			count++
		}
	}
	return m.min <= count && count <= m.max
}

func validator_two(m Meta) bool {
	p1 := m.min -1
	p2 := m.max -1
	return ((string(m.password[p1]) == m.char && string(m.password[p2]) != m.char) ||
	        (string(m.password[p1]) != m.char && string(m.password[p2]) == m.char))
}

func process_chunk(fn validator, lines []Meta, c chan int){
	total := 0
	for _, line := range(lines){
		if (fn(line)){
			total++
		}
	}
	c <- total
}

func chained_process_chunk(fn1 validator, fn2 validator, lines []Meta, c1 chan int, c2 chan int){
	t1 := 0
	t2 := 0
	for _, line := range(lines){
		if (fn1(line)){
			t1++
		}
		if fn2(line){
			t2++
		}
	}
	c1 <- t1
	c2 <- t2
}

func main() {
	c1 := make(chan int)
	c2 := make(chan int)

	var lines []Meta
	f, _ := os.Open("passwords.txt")
	scanner := bufio.NewScanner(f)
    for scanner.Scan() {
		m := make_meta(scanner.Text())
		lines = append(lines, m)
	}

	// go chained_process_chunk(validator_one, validator_two, lines[0:250], c1, c2)
	// go chained_process_chunk(validator_one, validator_two, lines[250:500], c1, c2)
	// go chained_process_chunk(validator_one, validator_two, lines[500:750], c1, c2)
	// go chained_process_chunk(validator_one, validator_two, lines[750:1000], c1, c2)
	// go process_chunk(validator_one, lines[0:250], c1)
	// go process_chunk(validator_one, lines[250:500], c1)
	// go process_chunk(validator_one, lines[500:750], c1)
	// go process_chunk(validator_one, lines[750:1000], c1)

	// go process_chunk(validator_two, lines[0:250], c2)
	// go process_chunk(validator_two, lines[250:500], c2)
	// go process_chunk(validator_two, lines[500:750], c2)
	// go process_chunk(validator_two, lines[750:1000], c2)

	total1 := <- c1
	total1 += <- c1
	total1 += <- c1
	total1 += <- c1

	total2 := <- c2
	total2 += <- c2
	total2 += <- c2
	total2 += <- c2

	fmt.Println("Part 1:", total1)
	fmt.Println("Part 2:", total2)
}
