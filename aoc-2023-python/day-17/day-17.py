import unittest
from queue import PriorityQueue


def parse_input(test=False):
    filename = "test.txt" if test else "input.txt"
    with open(filename) as f:
        grid = [[int(x) for x in line] for line in f.read().splitlines()]
    return grid


def part1(grid):
    pq = PriorityQueue()
    # (heat_loss, row, col, dir_row, dir_col, steps_in_dir)
    pq.put((0, 0, 0, 0, 0, 0))
    seen = set()

    while not pq.empty():
        hl, r, c, dr, dc, n = pq.get()

        if (r, c) == (len(grid) - 1, len(grid[0]) - 1):
            return hl

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))

        if n < 3 and (dr, dc) != (0, 0):
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                pq.put((hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr, nc = r + ndr, c + ndc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    pq.put((hl + grid[nr][nc], nr, nc, ndr, ndc, 1))

    return -1


def part2(grid):
    pq = PriorityQueue()
    seen = set()
    # (heat_loss, row, col, dir_row, dir_col, steps_in_dir)
    pq.put((0, 0, 0, 0, 0, 0))

    while not pq.empty():
        hl, r, c, dr, dc, n = pq.get()

        if r == len(grid) - 1 and c == len(grid[0]) - 1 and n >= 4:
            return hl

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))

        if n < 10 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                pq.put((hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

        if n >= 4 or (dr, dc) == (0, 0):
            for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        pq.put((hl + grid[nr][nc], nr, nc, ndr, ndc, 1))

    return -1


print(f"Part 1: {part1(parse_input())}")
print(f"Part 2: {part2(parse_input())}")


class TestDay17(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1(parse_input(test=True)), 102)

    def test_part2(self):
        self.assertEqual(part2(parse_input(test=True)), 94)


# Run the test
unittest.main()
