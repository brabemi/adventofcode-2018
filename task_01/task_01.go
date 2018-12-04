package main

import "fmt"

// part one
func partOne(numbers []int) int {
	sum := 0
	for _, num := range numbers {
		sum += num
	}
	return sum
}

// part two
func partTwo(numbers []int) int {
	sum := 0
	freqs := map[int]bool{sum: true}
	for true {
		for _, num := range numbers {
			sum += num
			if _, ok := freqs[sum]; !ok {
				freqs[sum] = true
			} else {
				return sum
			}
		}
	}
	// error
	return 0
}

func main() {
	var numbers []int
	var num int
	var err error

	_, err = fmt.Scanf("%d\n", &num)
	for err == nil {
		numbers = append(numbers, num)
		_, err = fmt.Scanf("%d\n", &num)
	}

	fmt.Println("Part 1 =", partOne(numbers))
	fmt.Println("Part 2 =", partTwo(numbers))
}
