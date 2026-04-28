target = 10
count = 0

nums = range(target)

while target > 0:
    if count % nums == 0:
        print(count)