# Title: 
# Problem Specification:
# Answer: 
# Approach 1:

import math

num = math.factorial(100)

# 1. Convert int to array of digits
digit_array = [int(digit) for digit in str(num)] # [1, 2, 3, 4, 5]

# 2. Sum all items in the array
total_sum = sum(digit_array)

print(total_sum) # Output: 15
