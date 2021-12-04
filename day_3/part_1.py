with open('input.txt') as f:
    lines = f.read().splitlines()

count_zero = 0
count_one = 0
gamma = ""
epsilon = ""

for i in range(len(lines[0])):
    count_zero = 0
    count_one = 0
    for index, item in enumerate(lines):
        if lines[index][i] == '0':
            count_zero += 1
        else:
            count_one += 1

    if count_zero > count_one:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))
