This class returns Primes numbers. The method first will return n firsts primes numbers.

For example:
Prime::first(1) = [2]
Prime::first(2) = [2, 3]
Prime::first(5) = [2, 3, 5, 7, 11]
array_slice(Prime::first(20).last(5), 0, -5) = [53, 59, 61, 67, 71]

Prime number: https://en.wikipedia.org/wiki/Prime_number