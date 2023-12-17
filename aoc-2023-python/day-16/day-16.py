from collections import deque
import unittest


def parse_input(test=False):
    filename = "test.txt" if test else "input.txt"
    with open(filename) as f:
        data = [list(x) for x in f.read().splitlines()]
    return data


def part1(data):
    """Returns number of energized tiles with BFS"""
    energized = set()
    state = [(0, -1, 0, 1)]

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


print(f"Part 1: {part1(parse_input())}")


class Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1(parse_input(test=True)), 46)


unittest.main()
