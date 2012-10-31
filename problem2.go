package main

/*
 *  Problem 2 from Project Euler
 *
 *  By considering the terms in the Fibonacci sequence whose values do not 
 *  exceed four million, find the sum of the even-valued terms.
 */

const N = 100

func main() {

}

func fibonacci() func(c chan <- int) {
    var f1, f2 = 0, 1
    f := func(c chan <- int) {
        f0 := f1
        f1, f2 = f2, f1+f2
        c <- f0
    }
    return f
}
