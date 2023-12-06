import re

lines = """
Time:        58     81     96     76
Distance:   434   1041   2219   1218
"""

time = int("".join([x for x in re.findall(r'\d+', lines.split('\n')[1])]))
distance = int("".join([x for x in re.findall(r'\d+', lines.split('\n')[2])]))

race = (time, distance)

margin = 0
time = race[0]
record = race[1]
for i in range(race[0]):
    distance = (time - i) * i
    if distance > record:
        margin += 1

print(margin)
