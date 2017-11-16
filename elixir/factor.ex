defmodule Factor do
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
