package main

/*
 *  Problem 2 from Project Euler
 *
 *  By considering the terms in the Fibonacci sequence whose values do not 
 *  exceed four million, find the sum of the even-valued terms.
 */

const N = 4000000

func main() {
	fib := fibonacci()
	i := fib()
	sum := 0

	for i < N {
		if i%2 == 0 {
			sum += i
		}
		i = fib()
	}

	println(sum)
}

func fibonacci() func() int {
	var f1, f2 = 0, 1
	f := func() int {
		f0 := f1
		f1, f2 = f2, f1+f2
		return f0
	}
	return f
}
