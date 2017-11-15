#!/usr/bin/env elixir

# Problem 5:
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

Code.load_file("factor.ex")

n = 20

defmodule Euler5 do
  def smallest_common_multiple(n) do
    n..1
    |> Enum.reduce(&Euler5.product/2)
    |> Euler5.divide_all_factors(n, n)
  end

  def divide_all_factors(total, 1, _) do
    total
  end
  def divide_all_factors(total, n, under) do
    test_total = div(total, n)

    if div_under(test_total, under) do
      divide_all_factors(test_total, n-1, under)
    else
      divide_all_factors(total, n-1, under)
    end
  end

  def div_under(_, 1),                             do: true
  def div_under(n, under) when rem(n, under) == 0, do: div_under(n, under-1)
  def div_under(n, under) when rem(n, under) > 0,  do: false

  def product(n, acc) do
    n * acc
  end
end

IO.inspect(Euler5.smallest_common_multiple(n))
