#!/usr/bin/env elixir

# Problem 4:
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

defmodule Euler do
  def largest_palindrome(digit_count) do
    Enum.max(filter_palindromes(digit_count))
  end

  def filter_palindromes(digit_count) do
    zipdigits(digit_count)
    |> Stream.map(fn({a, b}) -> a * b end)
    |> Stream.filter(&Euler.check_palindrome/1)
  end

  def check_pair(pair) do
    {left, right} = pair
    check_palindrome(left * right)
  end

  def zipdigits(digit_count) do
    nn = round(:math.pow(10, digit_count))
    Stream.zip(slow_iter(nn), fast_iter(nn))
  end

  # Returns nn iterations of nn
  defp slow_iter(nn) do
    Stream.map(Range.new(nn*nn-1, nn), fn(n) -> div(n, nn) end)
  end

  defp fast_iter(nn) do
    Range.new(nn-1, 0)
    |> Enum.to_list()
    |> Stream.cycle()
  end

  def concat_digits(digits) do
    Enum.reduce(digits, fn(n, acc) -> acc * 10 + n end)
  end

  def check_palindrome(n) do
    n == reverse_num(n)
  end

  def reverse_num(n) do
    concat_digits(reverse_num_arr(n))
  end

  defp reverse_num_arr(n) when n < 10 do
    [n]
  end
  defp reverse_num_arr(n) do
    [rem(n, 10) | reverse_num_arr(div(n, 10))]
  end
end

IO.inspect(Euler.largest_palindrome(3))
