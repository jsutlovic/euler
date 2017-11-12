#!/usr/bin/env elixir

# Problem 3:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

defmodule Euler do
  def prime_filter(n) do
    length(factorize(n)) > 0
  end

  def factorize(n) when n > 1 do
    divisor(n, 2, [])
  end
  def factorize(n) when n == 1, do: [1]

  defp divisor(n, i, factors) when n < i*i do
    factors
  end
  defp divisor(n, i, factors) when n == i*i do
    [i | factors]
  end
  defp divisor(n, i, factors) when rem(n, i) == 0 do
    divisor(n, i+1, [i, div(n, i) | factors])
  end
  defp divisor(n, i, factors) do
    divisor(n, i+1, factors)
  end
end

600851475143
# 13195
|> Euler.factorize()
|> Enum.reject(&Euler.prime_filter/1)
|> Enum.sort()
|> Enum.reverse()
|> hd
|> IO.inspect()
