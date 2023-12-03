import re

with open("input.txt", "r") as file:
    lines = file.readlines()

sum = 0
color_max = {"red": 12, "green": 13, "blue": 14}


def above_upper_bound(line, color):
    pattern = r"(\d+) " + color
    return max([int(x) for x in re.findall(pattern, line)]) > color_max[color]


for line in lines:
    game_id = re.findall(r"Game (\d+)", line)[0]
    if above_upper_bound(line, "red") or above_upper_bound(line, "green") or above_upper_bound(line, "blue"):
        continue
    sum += int(game_id)

print(sum)
