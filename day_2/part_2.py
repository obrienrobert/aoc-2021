horizontal_position = 0
depth = 0
aim = 0

with open('input.txt') as f:
    lines = f.read().splitlines()
    for index, item in enumerate(lines):
        if item.split()[0] == "forward":
            horizontal_position += int(item.split()[1])
            depth += aim * int(item.split()[1])
        elif item.split()[0] == "down":
            aim += int(item.split()[1])
        elif item.split()[0] == "up":
            aim -= int(item.split()[1])

print(horizontal_position * depth)
