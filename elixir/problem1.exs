#!/usr/bin/env elixir

# Problem 1:
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

defmodule Euler do
  def filter1(n, acc) when rem(n, 3) == 0, do: n + acc
  def filter1(n, acc) when rem(n, 5) == 0, do: n + acc
  def filter1(_, acc),                     do: acc
end

1..999
|> Enum.reduce(0, &Euler.filter1/2)
|> IO.puts()
