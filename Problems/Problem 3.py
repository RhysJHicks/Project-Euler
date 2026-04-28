# Problem

n = 600851475143
factor = 2
largest = 1

while factor * factor <= n:
    if n % factor == 0:
        largest = factor
        n //= factor
    else:
        factor += 1 if factor == 2 else 2

if n > 1:
    largest = n

print(largest)