horizontal_position = 0
depth = 0

with open('input.txt') as f:
    lines = f.read().splitlines()
    for index, item in enumerate(lines):
        if item.split()[0] == "forward":
            horizontal_position += int(item.split()[1])
        elif item.split()[0] == "down":
            depth += int(item.split()[1])
        elif item.split()[0] == "up":
            depth -= int(item.split()[1])

print(horizontal_position * depth)
