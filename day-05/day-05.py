import re


with open("input.txt", "r") as file:
    lines = file.readlines()


def map_seed(mapping, seed):
    correct_map = False
    for destination_start, source_start, length in mapping:
        if source_start <= seed < source_start + length:
            offset = seed - source_start
            return destination_start + offset
    return seed


def parse_input(lines):
    mappings = {}
    map_name = 'seeds'
    mappings[map_name] = [int(x) for x in lines[0].split(': ')[1].split(' ')]

    for line in lines[1:]:
        if 'map' in line:
            map_name = re.search(r'(\w+-to-\w+)', line).group(1)
            mappings[map_name] = []
        if re.search(r'\d', line):
            mappings[map_name].append([int(x) for x in line.split(' ')])

    for key, value in mappings.items():
        if key == 'seeds':
            continue
        mappings[key] = sorted(value, key=lambda x: x[0])
    return mappings


def convert_seeds(mappings):
    smallest_location = float('inf')  # Initialize with a very large number
    categories = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light',
                  'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

    for seed in mappings['seeds']:
        location = seed
        for category in categories:
            location = map_seed(mappings[category], location)

        if location < smallest_location:
            smallest_location = location

    return smallest_location


mappings = parse_input(lines)
print(convert_seeds(mappings))
