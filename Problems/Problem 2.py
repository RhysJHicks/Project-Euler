# Even Fibonacci Numbers
# Create Fibonacci, Check if even, Store in running count, Print total.
# Answer 4613732
# Good problem, good math, improvements through reduce checks, improvements through a third of the calculations.

target = 4000000
sample = 10
# sample = 44

# Works but is too inefficient
# Calculates every fibonacci number and checks each one
def fibonacci_iterative(nums):
    total = 0
    a, b = 0, 1
    for num in range(nums):
        a, b = b, a + b
        if a % 2 == 0:
            total += a
    print(total)

# Every third number is even, don't need to check
# Formula for calculating next even using prior evens
def fibonacci_recursive_even_skip(nums):
    total = 0
    a, b = 0, 2
    for num in range(nums//3):
        a, b = b, 4 * b + a
        total += a
        if b > 4000000:
            break
    print(total)

# fibonacci_iterative(sample)
fibonacci_recursive_even_skip(target)