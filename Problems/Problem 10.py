# Find the sum of all the primes below two million?

from sympy import primerange

example = 10
target = 2000000

primes = list(primerange(1,target))

print(sum(primes))

# Answer: 142913828922