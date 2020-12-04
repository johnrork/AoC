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

func make_meta(line string) Meta {
	policy_and_password := strings.Split(line, ": ")
	numbers_and_char := strings.Split(policy_and_password[0], " ")
	min_and_max := strings.Split(numbers_and_char[0], "-")
	min, _ := strconv.Atoi(min_and_max[0])
	max, _ := strconv.Atoi(min_and_max[1])
	return Meta{min, max, numbers_and_char[1], policy_and_password[1]}
}

func validator_one(line string) bool {
	m := make_meta(line)
	count := 0
	for _, c := range(m.password) {
		if (string(c) == m.char){
			count++
		}
	}
	return m.min <= count  && count <= m.max
}

func validator_two(line string) bool {
	m := make_meta(line)
	p1 := m.min -1
	p2 := m.max -1
	return ((string(m.password[p1]) == m.char && string(m.password[p2]) != m.char) ||
	        (string(m.password[p1]) != m.char && string(m.password[p2]) == m.char))
}

func main() {
	total1 := 0
	total2 := 0
	scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
		v := scanner.Text()
		if (validator_one(v)){
			total1++
		}
		if (validator_two(v)){
			total2++
		}
	}
	fmt.Println("Part 1:", total1)
	fmt.Println("Part 2:", total2)
}
