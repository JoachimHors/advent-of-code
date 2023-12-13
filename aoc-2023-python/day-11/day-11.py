def load_input(test=False):
    filename = 'test.txt' if test else 'input.txt'
    with open(filename, 'r') as file:
        lines = file.readlines()
        grid = [list(line.replace('\n', '')) for line in lines]
    return grid


def expand_grid(lines, part2=False):
    for i in range(len(lines) - 1, -1, -1):
        if '#' not in lines[i] and 'X':
            if part2:
                lines[i] = list('X' * len(lines[i]))
            else:
                lines.insert(i, list('.' * len(lines[i])))
        if '#' not in [line[i] for line in lines]:
            for line in lines:
                if part2:
                    line[i] = 'X'
                else:
                    line.insert(i, '.')
    return lines


def get_galaxies(lines):
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                galaxies.append((i, j))
    return galaxies


def get_distance(grid, galaxy1, galaxy2, part2=False):
    distance = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    if not part2:
        return distance
    path = []
    for i in range(distance):
        if galaxy1[0] < galaxy2[0]:
            galaxy1 = (galaxy1[0] + 1, galaxy1[1])
        elif galaxy1[0] > galaxy2[0]:
            galaxy1 = (galaxy1[0] - 1, galaxy1[1])
        elif galaxy1[1] < galaxy2[1]:
            galaxy1 = (galaxy1[0], galaxy1[1] + 1)
        elif galaxy1[1] > galaxy2[1]:
            galaxy1 = (galaxy1[0], galaxy1[1] - 1)
        path.append(grid[galaxy1[0]][galaxy1[1]])

    steps = sum([1 if point != 'X' else 1000000 for point in path])
    return steps


def sum_distances(grid, galaxies, part2=False):
    sum = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            sum += get_distance(grid, galaxies[i], galaxies[j], part2)
    return sum


def part_1(test=False):
    grid = load_input(test)

    expanded_grid = expand_grid(grid)

    galaxies = get_galaxies(expanded_grid)
    print(f"Part 1: {sum_distances(grid, galaxies)}")


def part_2(test=False):
    grid = load_input(test)

    expanded_grid = expand_grid(grid, part2=True)

    galaxies = get_galaxies(expanded_grid)
    print(f"Part 2: {sum_distances(grid, galaxies, part2=True)}")


part_1()
part_2()
