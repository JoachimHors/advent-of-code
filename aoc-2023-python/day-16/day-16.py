from collections import deque
import unittest


def parse_input(test=False):
    filename = "test.txt" if test else "input.txt"
    with open(filename) as f:
        data = [list(x) for x in f.read().splitlines()]
    return data


def part1(data, state=[(0, -1, 0, 1)]):
    """Returns number of energized tiles with BFS"""

    energized = set()
    queue = deque(state)

    while queue:
        x, y, x_dir, y_dir = queue.popleft()

        x += x_dir
        y += y_dir

        if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]):
            continue

        current_tile = data[x][y]

        if current_tile == "." or current_tile == "-" and x_dir == 0 or current_tile == "|" and y_dir == 0:
            if (x, y, x_dir, y_dir) not in energized:
                energized.add((x, y, x_dir, y_dir))
                queue.append((x, y, x_dir, y_dir))

        elif current_tile == "/":
            x_dir, y_dir = (-y_dir, -x_dir)
            if (x, y, x_dir, y_dir) not in energized:
                energized.add((x, y, x_dir, y_dir))
                queue.append((x, y, x_dir, y_dir))

        elif current_tile == "\\":
            x_dir, y_dir = (y_dir, x_dir)
            if (x, y, x_dir, y_dir) not in energized:
                energized.add((x, y, x_dir, y_dir))
                queue.append((x, y, x_dir, y_dir))

        else:
            for x_dir, y_dir in [(1, 0), (-1, 0)] if current_tile == "|" else [(0, 1), (0, -1)]:
                if (x, y, x_dir, y_dir) not in energized:
                    energized.add((x, y, x_dir, y_dir))
                    queue.append((x, y, x_dir, y_dir))

    return len({(x, y) for (x, y, _, _) in energized})


def part2(data):
    max_engergized = 0
    for i in range(len(data)):
        top = part1(data, state=[(i, -1, 0, 1)])
        bottom = part1(data, state=[(i, len(data[0]), 0, -1)])
        max_engergized = max(max_engergized, top, bottom)

    for i in range(len(data[0])):
        left = part1(data, state=[(-1, i, 1, 0)])
        right = part1(data, state=[(len(data), i, -1, 0)])
        max_engergized = max(max_engergized, left, right)

    return max_engergized


print(f"Part 1: {part1(parse_input())}")
print(f"Part 2: {part2(parse_input())}")


class Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1(parse_input(test=True)), 46)

    def test_part2(self):
        self.assertEqual(part2(parse_input(test=True)), 51)


unittest.main()
