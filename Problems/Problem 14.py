# Title: Longest Collatz Sequence
# Problem Specification:
# Answer: 
# Approach 1:

def get_collatz_length(n: int) -> int:
    """Calculates the total length of the Collatz sequence for n."""
    count = 1
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count += 1
    return count

# 1. Print header
print(f"{'Start':<8} | {'Sequence Length':<15}")
print("-" * 28)

# 2. Loop and print lengths for numbers 1 to 100
for i in range(1, 1000001):
    length = get_collatz_length(i)
    print(f"{i:<8} | {length:<15}")

# 3. Print a quick summary at the bottom
print("-" * 28)
lengths_dict = {i: get_collatz_length(i) for i in range(1, 101)}
longest_num = max(lengths_dict, key=lengths_dict.get)

print(f"Longest Sequence: Number {longest_num} ({lengths_dict[longest_num]} steps)")
