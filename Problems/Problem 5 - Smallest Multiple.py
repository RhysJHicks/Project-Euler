# Problem 5: Smallest Multiple
# Answer: 232792560
# Problem Specification: Smallest Possible divisible of all numbers from 1 to 20, This is the same as what is common multiple.
# Approach 1: Brute Force


def approach_1():
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return (a * b) // gcd(a, b)

    number = 1
    for i in range(1, 21):
        number = lcm(number, i)

    print(number)

approach_1()