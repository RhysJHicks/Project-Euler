# Problem 5: Smallest Multiple
# Problem Specification: Smallest Possible divisible of all numbers from 1 to 20, This is the same as what is common multiple.
# Example: range 1 to 10, has 2520 as the smallest evenly divisible
#
# Approach 1: Brute Force
# Approach Rational:
#
# Approach 2: Improved Brute Force
# App
#
# Approach 3: Prisadhkl



def approach_1():
    total = 1
    nums = range(11, 20)
    for i in nums:
        total *= i

    print(total)

# approach_1()