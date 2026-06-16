# Problem 5: Smallest Multiple
# Problem Specification: Smallest Possible divisible of all numbers from 1 to 20, This is the same as what is common multiple.
# Approach 1: Brute Force


def approach_1():
    nums = range(1, 11)
    while True:
        for i in nums:
            if i % 2 != 0:
                continue

approach_1()