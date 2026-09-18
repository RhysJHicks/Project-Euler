"""Project Euler Problem 12
    Problem Specification:
    Answer:
    Approach 1:
"""


def count_factors(n):
    """Generates a list of all divisors and returns the count"""
    return len([i for i in range(1, n + 1) if n % i == 0])


def approach_1(target_len) -> int:
    """This is the First approach
    >>> approach_1(5)
    7
    >>> approach_1(2)
    2

    """
    length = 0
    i = 0
    total = 0
    while length < target_len:
        i += 1
        total += i
        length = count_factors(total)

    return i


print(approach_1(20))
