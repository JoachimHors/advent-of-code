
def expand_grid(lines):
    for i in range(len(lines) - 1, -1, -1):
        if '#' not in lines[i]:
            lines.insert(i, list('.' * len(lines[i])))
        if '#' not in [line[i] for line in lines]:
            for line in lines:
                line.insert(i, '.')
    return lines


def get_galaxies(lines):
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                galaxies.append((i, j))
    return galaxies


def get_distance(galaxy1, galaxy2):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


def sum_distances(galaxies):
    sum = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            sum += get_distance(galaxies[i], galaxies[j])
    return sum


with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [list(line.replace('\n', '')) for line in lines]

expanded_grid = expand_grid(lines)
galaxies = get_galaxies(expanded_grid)
print(sum_distances(galaxies))
