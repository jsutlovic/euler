#!/usr/bin/env elixir

# Problem 3:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

Code.load_file("factor.ex")

defmodule Euler3 do
  def largest_prime_factor(n) do
    n
    |> Factor.factorize()
    |> Enum.reject(&Factor.prime_filter/1)
    |> Enum.sort()
    |> Enum.reverse()
    |> hd
  end
end

IO.inspect(Euler3.largest_prime_factor(600851475143))
