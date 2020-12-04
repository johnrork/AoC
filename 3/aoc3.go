package main

import (
	"bufio"
	"fmt"
	"os"
)

func toboggan(lines []string, over int, down int) int {
	offset := 0
	count := 0
	last_line := 0
	ln_length := len(lines[0])

	for i, l := range lines {
		if last_line+down != i {
			continue
		}
		offset += over
		if offset >= ln_length {
			offset = offset - ln_length
		}
		if string(l[offset]) == "#" {
			count = count + 1
		}
		last_line = i
	}
	return count
}

func main() {
	f, _ := os.Open("trees.txt")
	scanner := bufio.NewScanner(f)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	t1 := toboggan(lines, 1, 1)
	t2 := toboggan(lines, 3, 1)
	t3 := toboggan(lines, 5, 1)
	t4 := toboggan(lines, 7, 1)
	t5 := toboggan(lines, 1, 2)

	fmt.Println("Part 1", t2)
	fmt.Println("Part 2:", t1*t2*t3*t4*t5)
}
