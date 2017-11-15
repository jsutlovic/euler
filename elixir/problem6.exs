#!/usr/bin/env elixir

# Problem 6:
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

n = 100

defmodule Euler6 do
  def diff_squares(n) do
    square_sums(n) - sum_squares(n)
  end

  def sum_squares(n) do
    1..n
    |> Enum.map(&Euler6.square/1)
    |> Enum.sum()
  end

  def square_sums(n) do
    1..n
    |> Enum.sum()
    |> Euler6.square()
  end

  def square(n) do
    n * n
  end
end

IO.inspect(Euler6.diff_squares(n))
