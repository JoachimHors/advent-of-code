from functools import reduce


class Number(object):
    def __init__(self, value, line, start, end):
        self.value = value
        self.line = line
        self.start = start
        self.end = end


with open("input.txt", "r") as file:
    lines = file.readlines()

# Initialize a list of numbers
numbers = []
for index, line in enumerate(lines):
    i = 0
    while i < len(line):
        if not line[i].isdecimal():
            i += 1
            continue
        start = i
        number = ""
        while line[i].isdecimal() and i < len(line):
            number += line[i]
            i += 1
        end = i
        numbers.append(Number(int(number), int(index), int(start), int(end)))

gears = {}
for num in numbers:
    for i in range(num.line - 1, num.line + 2):
        if i < 0 or i >= len(lines):
            continue
        for j in range(num.start - 1, num.end + 1):
            if j < 0 or j >= len(lines[0]):
                continue
            if lines[i][j] != "*":
                continue
            if not gears.get((i, j)):
                gears[(i, j)] = []
            gears[(i, j)].append(num.value)

gear_ratio_sum = 0
for gear in gears:
    if len(gears[gear]) == 2:
        gear_ratio_sum += reduce(lambda a, b: a * b, gears[gear])

print(gear_ratio_sum)
