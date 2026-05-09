example = 10
actual = 1000
total = 0

for i in range(1, actual):
    if i % 5 == 0 or i % 3 == 0:
        total += i

print(total)
