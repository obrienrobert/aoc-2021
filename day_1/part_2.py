total_increases = 0

with open('./measurements.txt') as f:
    lines = f.read().splitlines()

for i in range(len(lines) - 3 + 1):
    total = int(lines[i + 0]) + int(lines[i + 1]) + int(lines[i + 2])
    if total > int(lines[i + -1]) + int(lines[i + 0]) + int(lines[i + 1]):
        total_increases += 1

print(total_increases)
