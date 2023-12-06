import re

lines = """
Time:        58     81     96     76
Distance:   434   1041   2219   1218
"""

times = [int(x) for x in re.findall(r'\d+', lines.split('\n')[1])]
distances = [int(x) for x in re.findall(r'\d+', lines.split('\n')[2])]

races = list(zip(times, distances))

sum = 1
for race in races:
    margin = 0
    time = race[0]
    record = race[1]
    for i in range(race[0]):
        distance = (time - i) * i
        if distance > record:
            margin += 1
    sum *= margin

print(sum)
