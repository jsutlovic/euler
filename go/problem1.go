package main

/*
 *  Problem 1 from Project Euler
 *
 *  Find the sum of all the multiples of 3 or 5 below 1000.
 */

const N = 1000

func main() {
	sum := 0
	for i := 0; i < N; i++ {
		if (i%3 == 0) || (i%5 == 0) {
			sum += i
		}
	}
	println(sum)
}
