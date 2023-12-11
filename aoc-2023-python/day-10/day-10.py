def parse_input(file_name):
    """ Parse the input data to create the maze grid. """
    with open(file_name) as f:
        input_data = f.read()
        grid = [list(line) for line in input_data.split('\n')]
    return grid


def find_start_position(grid):
    """ Find the start position in the grid. """
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                return x, y
    return None


def valid_directions(pipe):
    """ Return valid directions based on the pipe type. """
    return {
        "|": ["N", "S"],
        "-": ["E", "W"],
        "J": ["N", "W"],
        "L": ["N", "E"],
        "7": ["S", "W"],
        "F": ["S", "E"],
        "S": ["N", "S", "E", "W"],
    }.get(pipe, [])


def valid_pipes_from_direction(direction):
    """ Return valid pipes for a given direction. """
    return {
        "N": ["|", "7", "F"],
        "S": ["|", "J", "L"],
        "E": ["-", "J", "7"],
        "W": ["-", "F", "L"],
    }.get(direction, [])


def bfs_longest_path(grid, start):
    """ Perform BFS to find the longest path from start. """
    moves = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
    queue = [start]
    visited = set()
    distances = {start: 0}
    max_distance = 0

    while queue:
        x, y = queue.pop(0)
        visited.add((x, y))

        for direction in valid_directions(grid[y][x]):
            dx, dy = moves[direction]
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] in valid_pipes_from_direction(direction):
                if (nx, ny) not in visited:
                    queue.append((nx, ny))
                    distances[(nx, ny)] = distances[(x, y)] + 1
                    max_distance = max(max_distance, distances[(nx, ny)])

    return max_distance


grid = parse_input('input.txt')
start = find_start_position(grid)
print(f"Part 1: {bfs_longest_path(grid, start)}")
