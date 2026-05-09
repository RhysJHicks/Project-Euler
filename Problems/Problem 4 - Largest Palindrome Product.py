# Largest Palindrome Product
# Answer: 906609

# The range of possible answers is (999x999) - (100x100) = 985680
# There is only 809,100 different permutations off n=999, r= 2, w/no repeats

# Approach 1 - *Smart* Brute force
#   Start at the highest Number pairing possible, If the current highest palindrome is higher than the current total ignore
# Approach 1 rational:
#   The amount of permutations and the range of total values is not too much when a majority of those combinations will be skipped.
#   Total of 9193 permutations where explored, 1 = ?, 2 = 132, 3 = 9193, 4 = 13,947, 5 = 1,102,168

from sympy.ntheory import is_palindromic
largest_palindrome = 0
total = 0
for n in range(999, 100, -1):
    for m in range(999, 100, -1):
        total = n*m
        if total < largest_palindrome:
            break
        if is_palindromic(total):
            largest_palindrome = total
            break
print(largest_palindrome)