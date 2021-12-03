total_increases = 0

with open('./measurements.txt') as f:
    lines = f.read().splitlines()

    for index, item in enumerate(lines[0:]):
        if int(item) > int(lines[index - 1]):
            total_increases += 1

print(total_increases)
