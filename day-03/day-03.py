import re


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

# Sum all valid part numbers
sum = 0
pattern = r"[^\.|\d]"
for number in numbers:
    left = number.start - 1 if number.start > 0 else 0
    right = number.end + 1 if number.end + \
        1 < len(lines[number.line]) else number.end
    top = number.line - 1 if number.line > 0 else 0
    bottom = number.line + 1 if number.line + 1 < len(lines) else number.line

    box_lines = lines[top:bottom + 1]
    box_string = "".join([x[left:right] for x in box_lines])
    if re.search(pattern, box_string):
        sum += number.value

print(sum)
