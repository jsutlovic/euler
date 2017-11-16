#!/usr/bin/env elixir

# Problem 7:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

n = 10_001

Code.load_file("factor.ex")

defmodule Euler7 do
  def nth_prime(n) do
    hd(nth_prime_list([], 2, n))
  end

  defp nth_prime_list(primes, _, 0) do
    primes
  end
  defp nth_prime_list(primes, i, n) do
    factors = Factor.factorize(i)
    case length(factors) do
      0 ->
        nth_prime_list([i | primes], i+1, n-1)
      _ ->
        nth_prime_list(primes, i+1, n)
    end
  end
end

IO.inspect(Euler7.nth_prime(n))
