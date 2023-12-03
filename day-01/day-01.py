import re

with open("input.txt", "r") as file:
    lines = file.readlines()

sum = 0

for line in lines:
    digits = re.findall(r"\d", line)
    sum += int(digits[0] + digits[-1])

print(sum)
