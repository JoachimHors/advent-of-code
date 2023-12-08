import re

with open("input.txt", "r") as file:
    lines = file.readlines()

sum = 0


def find_upper_bound(line, color):
    pattern = r"(\d+) " + color
    return max([int(x) for x in re.findall(pattern, line)])


for line in lines:
    sum += find_upper_bound(line, "red") * find_upper_bound(line,
                                                            "green") * find_upper_bound(line, "blue")

print(sum)
