import unittest
import re


def parse_input(test=False, part1=True):
    filename = "test.txt" if test else "input.txt"
    with open(filename) as f:
        if part1:
            return [x.split() for x in f.read().splitlines()]
        else:
            lines = [x.split() for x in f.read().splitlines()]
            instructions = []
            for line in lines:
                directions = {
                    "0": "R",
                    "1": "D",
                    "2": "L",
                    "3": "U",
                }
                hexadecimal = re.sub(r"\#|\(|\)", "", line[2])
                direction = directions[hexadecimal[-1]]
                distance = int(hexadecimal[:-1], 16)
                instructions.append((direction, distance))
            return instructions


def calculate_volume(instructions):
    def get_points(instructions):
        directions = {
            "R": (1, 0),
            "L": (-1, 0),
            "U": (0, -1),
            "D": (0, 1),
        }
        points = [(0, 0)]
        for instruction in instructions:
            # (x, y, distance)
            points.append((points[-1][0] + directions[instruction[0]][0] * int(instruction[1]),
                          points[-1][1] + directions[instruction[0]][1] * int(instruction[1]), int(instruction[1])))
        return points

    def calculate_area(points):
        """Calculate the area of a polygon using the Shoelace algorithm and Pick's theorem"""
        vertices = len(points)
        boundary_points = sum(int(x[-1]) for x in points)
        area = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) %
                   vertices][1]) for i in range(len(points) - 1)) / 2)
        interior_points = area - boundary_points // 2 + 1
        return int(interior_points + boundary_points)

    points = get_points(instructions)
    return calculate_area(points)


print(f"Part 1: {calculate_volume(parse_input())}")
print(f"Part 2: {calculate_volume(parse_input(part1=False))}")


class TestDay18(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(calculate_volume(parse_input(test=True)), 62)

    def test_part2(self):
        self.assertEqual(calculate_volume(
            parse_input(test=True, part1=False)), 952408144115)


unittest.main()
